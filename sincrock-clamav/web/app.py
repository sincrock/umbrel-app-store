from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Caminho interno onde o contêiner vai ler o log
LOG_PATH = "/data/logs/clamav_scan.log"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel ClamAV - Alertas</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #1a1a1a; color: #e0e0e0; padding: 20px; margin: 0; }
        .container { max-width: 900px; margin: 0 auto; }
        h1 { color: #fff; border-bottom: 2px solid #333; padding-bottom: 10px; }
        .alert-box { background-color: #2d1f1f; border-left: 5px solid #ff4444; padding: 15px; margin-bottom: 15px; border-radius: 4px; }
        .alert-title { font-weight: bold; color: #ff6666; margin-bottom: 5px; }
        .clean-box { background-color: #1f2d1f; border-left: 5px solid #00c851; padding: 10px; margin-bottom: 10px; border-radius: 4px; font-size: 14px; }
        .log-raw { background-color: #111; padding: 15px; border-radius: 4px; font-family: monospace; overflow-x: auto; white-space: pre-wrap; font-size: 13px; border: 1px solid #333; max-height: 400px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ Central de Alertas Antivírus (ClamAV)</h1>
        
        <h2>🚨 Ameaças Detectadas</h2>
        {% if alerts %}
            {% for alert in alerts %}
                <div class="alert-box">
                    <div class="alert-title">Item Infectado / Suspeito</div>
                    <div>{{ alert }}</div>
                </div>
            {% endfor %}
        {% else %}
            <p style="color: #00c851;">🎉 Nenhuma ameaça detectada até o momento. Sistema limpo!</p>
        {% endif %}

        <h2>📄 Histórico Recente do Log</h2>
        <div class="log-raw">{{ log_content }}</div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    alerts = []
    log_content = "Nenhum registro encontrado ainda."
    
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            # Pega as últimas 100 linhas para o histórico
            log_content = "".join(lines[-100:])
            # Filtra apenas as linhas de alerta real
            alerts = [line.strip() for line in lines if "ALERTA:" in line or "FOUND" in line]

    return render_template_string(HTML_TEMPLATE, alerts=alerts[::-1], log_content=log_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
