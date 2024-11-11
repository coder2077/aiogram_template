# Telegram Bot Template with aiogram, FastAPI, and asyncpg

This template project demonstrates how to build a Telegram bot with `aiogram` and set up a webhook using `FastAPI`, while using `asyncpg` for database interaction

## Steps to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/coder2077/aiogram-template.git
   cd aiogram-template
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate  # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run ngrok to expose the local server:
   ```bash
   ngrok http 8000
   ```

5. Modify `data.py` to configure parameters.

6. Start the server:
   ```bash
   uvicorn app.main:app --port 8000
   ```

The bot will now be running, send /start to the bot.
