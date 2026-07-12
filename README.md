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

Para adicionar esta loja ao seu servidor Umbrel, siga os passos abaixo:

1. Acesse o seu servidor Umbrel via **SSH**:
```bash
ssh umbrel@umbrel.local
```
*(Substitua `umbrel.local` pelo IP do seu servidor se necessário)*

2. Execute o comando oficial do Umbrel para adicionar repositórios de terceiros:
```bash
sudo umbrel-app-store repo add https://github.com/sincrock/umbrel-app-store.git
```

3. Abra a interface web do seu Umbrel, acesse a **App Store** e os novos aplicativos estarão disponíveis para instalação com um único clique!

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
