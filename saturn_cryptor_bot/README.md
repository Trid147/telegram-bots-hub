# 🪐 Saturn Cryptor Bot

A clean, multi-user Telegram bot written in Python that provides on-the-fly text and standalone file encryption (.txt, .png, .docx, etc.) using a multi-character bitwise **XOR (Exclusive OR)** symmetric cipher.

This bot features isolated per-user memory tracking, handles raw binary files safely in RAM using in-memory byte buffers (`io.BytesIO`), and includes structural configurations to easily bypass Deep Packet Inspection (DPI) network blocks via Cloudflare Workers.

---

## ✨ Features

- **Isolated Multi-User State:** Tracks distinct master keys safely inside memory dictionaries mapped strictly to individual Telegram Chat IDs (`USER_KEYS`). One user changing their key will never compromise another user's active session data.
- **In-Memory Binary Streaming:** Processes complex files (images, documents, archives) directly inside system RAM arrays using `io.BytesIO`. It leaves zero digital footprint or temporary unencrypted files on your host server storage.
- **Symmetric Cipher Restoration:** Because XOR math is perfectly self-inverting, sending an encrypted message or file through the bot a second time using the exact same master-key instantly restores it to its original, functional state.
- **Censorship Hardening Ready:** Includes structural endpoint anchors to easily connect a personal Cloudflare Worker routing proxy, allowing the bot server to operate seamlessly from restricted network regions.

---

## 🛠️ How to Deploy

### 1. Register the Bot
1. Search for `@BotFather` on Telegram and send the `/newbot` command.
2. Follow the prompt to name your bot and copy your unique **Authentication Token**.
3. Paste the token into the `TOKEN` variable inside `bot.py`.

### 2. Network Bypass Configuration (Optional)
If your host machine is deployed behind network regions blocking direct communication with `api.telegram.org`:
1. Create a free **Cloudflare Worker** using the proxy mirror script located in the master repository directory.
2. Update the endpoint definitions inside `bot.py` to route traffic through your custom edge proxy domain:
   ```python
   PROXY_URL = 'https://workers.dev{0}/{1}'
   PROXY_FILE_URL = 'https://workers.dev{0}/{1}'
   ```
*Note: Leave these strings blank if your network environment connects directly to official Telegram APIs.*

### 3. Initialize Server Environment
1. Ensure your host machine has isolated runtime spaces configured:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install telebot
   ```
2. Launch the script locally to confirm operational loops function correctly:
   ```bash
   python3 cryptor.py
   ```

---

## 🕹️ Conversational Interface Usage

Interact with Saturn Cryptor by issuing control strings in your private chat window:

1. **Set Active Encryption Key:**
   Send `/key [your-master-key]` (e.g., `/key MySecretKey123`). The bot will isolate this key exclusively to your chat handle.
   
2. **Encrypt/Decrypt Text Strings:**
   Simply type any plain message. The bot will encrypt it and return an absolute space-separated numeric cipher string marked with a `G# ` visual header prefix. Paste that exact `G# ` cipher text back to decrypt it.

3. **Encrypt/Decrypt Standalone Files:**
   Upload any item as an **uncompressed Document file** (do not send images as compressed photos, or Telegram will compress the image payload matrix). The bot downloads, processes, alters individual bytes, and returns a secure, encrypted copy of your file with the extension intact.

---

## 📋 Infrastructure: Systemd Service Unit File
To ensure your bot stays online indefinitely on a Linux VDS/VPS server and recovers automatically if the machine crashes or reboots, create a system daemon unit configuration at `/etc/systemd/system/saturn_cryptor.service`:

```ini
[Unit]
Description=Saturn Cryptor Bot Background Engine
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/telegram-bots-hub/saturn_cryptor_bot
ExecStart=/root/telegram-bots-hub/saturn_cryptor_bot/venv/bin/python3 bot.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
