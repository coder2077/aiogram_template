# Aiogram Webhook with FastAPI and asyncpg

This repository demonstrates how to set up an `aiogram` webhook with `FastAPI` and `asyncpg` for Telegram bot deployment.

## Steps to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/aiogram-fastapi-webhook.git
   cd aiogram-fastapi-webhook
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

5. Open the generated ngrok URL and update the `WEBHOOK_URL` in `data.py` to match the ngrok URL.

6. Modify `data.py` to configure your database connection and other bot parameters.

7. Start the server:
   ```bash
   uvicorn app.main:app --port 8000
   ```

The bot will now be running and ready to accept webhook requests.

## Important Notes

- Make sure you have a valid `asyncpg` connection set up in `data.py`.
- The bot will use ngrok to forward incoming requests to your local FastAPI server.
