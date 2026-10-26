# Telegram Bots Hub

Welcome to my Telegram Bots Hub! This repository is a curated mono-portfolio featuring automated, interactive, and infrastructure-optimized chat tools designed across multiple tech stacks. 

Every project in this hub is developed with a production-ready mindset, showcasing automated testing pipelines, reverse-proxy network engineering, and isolated service deployment configurations.

## How to Explore & Run

### Option 1: Isolate & Download a Single Bot
If you only need to explore or deploy a single bot directory from this repository without fetching the whole collection, you can use **[DownGit](https://minhaskamal.github.io/DownGit/#/home)**:
1. Open the specific folder of the bot you want here on GitHub.
2. Copy the URL path from your browser's address bar.
3. Paste that link directly into **DownGit** and extract a standalone ZIP archive.

### Option 2: Clone and Run Locally
To run and modify these bots on your local machine:
1. Clone the repository and navigate into your target project directory:
   ```bash
   git clone https://github.com/Trid147/telegram-bots-hubs
   cd telegram-bots-hub/bot_name_1
   ```
2. Initialize an isolated virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install the dependencies verified by the automated testing track:
   ```bash
   pip install -r requirements.txt
   ```
4. Each bot contains its own specific local `README.md` guide explaining token environment declarations and infrastructure hosting parameters.


