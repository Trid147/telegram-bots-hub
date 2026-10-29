# 🪐 Saturn Cryptor Bot

A multi-user Telegram bot in Python providing text and file encryption via a multi-character bitwise XOR symmetric cipher, featuring isolated per-user memory tracking and in-memory binary streaming.

---

## ✨ Features

- **Isolated Multi-User State:** Tracks distinct master keys mapped to individual Telegram Chat IDs.
- **In-Memory Binary Streaming:** Processes payloads via `io.BytesIO` without unencrypted disk caching.
- **Rootless Containerization:** Runs securely in unprivileged spaces using Podman.
- **Automated Deployment:** Includes Ansible IaC blueprints for server orchestration and systemd lifecycle management.

---

## 🚀 One-Command Automated Cloud Deployment

Deploy efficiently to a remote Linux VDS/VPS using the provided Ansible playbook.

### Prerequisites

Install Ansible and share your SSH public key:

For Debian/Ubuntu:
```bash
sudo apt install -y ansible
ssh-copy-id root@YOUR_SERVER_IP_ADDRESS
```

For Fedora:
```bash
sudo dnf install -y ansible
ssh-copy-id root@YOUR_SERVER_IP_ADDRESS
```

### Deployment Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Trid147/telegram-bots-hub/saturn_cryptor_bot
   cd telegram-bots-hub/saturn_cryptor_bot
   ```
2. **Configure `inventory.ini`** with your VDS public IP address.
3. **Execute the automation pipeline:**
   ```bash
   ansible-playbook -i inventory.ini deploy-bot.yml -e \
     "env_bot_token='YOUR_TELEGRAM_BOT_TOKEN' \
      env_proxy_url='https://workers.dev{0}/{1}' \
      env_proxy_file_url='https://workers.dev{0}/{1}'"
   ```

---

## 🛠 Manual Local / Development Deployment

1. Obtain a bot token from `@BotFather`.
2. Set up the local virtual environment and dependencies.
3. Export `TELEGRAM_BOT_TOKEN` and run `python3 cryptor.py`.

---

## 🕹 Conversational Interface Usage

- **Set Active Encryption Key:** Send `/key [your-master-key]`.
- **Encrypt/Decrypt Text Strings:** Type messages to receive a `G# ` numeric cipher string.
- **Encrypt/Decrypt Standalone Files:** Upload documents to receive secure encrypted copies.
