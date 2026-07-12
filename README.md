# 🌌 sincrock - Umbrel App Store

Repositório de aplicativos comunitários e customizados para o ecossistema **Umbrel / UmbrelOS**. O foco desta loja é trazer ferramentas de segurança, monitoramento e utilitários integrados de forma nativa ao sistema.

---

## 🛠️ Aplicativos Disponíveis

| Ícone | Nome do App | Descrição |
| :---: | :--- | :--- |
| <img src="icons/clam-av.svg" width="35" height="35"> | **ClamAV Scanner** | Antivírus open-source configurado para escanear automaticamente o armazenamento central e a pasta de downloads global do Umbrel. |
| <img src="icons/crowdsec.svg" width="35" height="35"> | **CrowdSec** | Sistema de detecção e prevenção de intrusões (IDS/IPS) que analisa logs de apps para mitigar ataques em tempo real. |

---

## 🚀 Como Instalar no seu Umbrel

Para adicionar esta loja ao seu servidor Umbrel, siga os passos abaixo diretamente pela interface gráfica:

1. Acesse o painel web do seu **Umbrel** no navegador.
2. Abra o aplicativo da **App Store**.
3. No canto superior direito, clique no menu de **três pontinhos (...)**.
4. Selecione a opção **Community App Stores**.
5. Insira a URL do repositório abaixo e clique em **Add**:
```text
https://github.com/sincrock/umbrel-app-store
```

Pronto! Os novos aplicativos estarão disponíveis na loja para instalação com um único clique.

---

## 🛠️ Desenvolvimento & Contribuição

Se você quiser testar modificações localmente no seu ecossistema Docker/Umbrel ou debugar os arquivos `docker-compose.yml`, sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request*.

### Estrutura do Repositório:
```text
umbrel-app-store/
├── icons/               # Ícones visuais dos apps (.svg)
├── sincrock-clamav/     # Manifesto e Compose do ClamAV
└── sincrock-crowdsec/   # Manifesto e Compose do CrowdSec
```

---
**Mantido por [sincrock](https://github.com/sincrock)** 🚀