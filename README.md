# Aiogram Webhook Example with FastAPI and asyncpg

This project demonstrates an Aiogram bot setup using FastAPI as the webhook server and asyncpg for PostgreSQL interactions.

## Setup and Run Instructions

1. **Clone the Repository and Navigate to the Project Folder**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
Set Up a Virtual Environment

bash
Copy code
python3 -m venv venv && source venv/bin/activate
Install Requirements

bash
Copy code
pip install -r requirements.txt
Run Ngrok on Port 8000
Ngrok is required to expose your FastAPI app to the public internet, which is necessary for the Telegram webhook.

bash
Copy code
ngrok http 8000
Ngrok will output a public URL like https://<subdomain>.ngrok.io. Note this URL, as it will be used for setting up the Telegram webhook.

Configure the Application Edit config.py and add your bot token, database settings, and the Ngrok URL you received in the previous step:

python
Copy code
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
DATABASE_URL = 'YOUR_DATABASE_URL_HERE'
WEBHOOK_URL = 'https://<subdomain>.ngrok.io/webhook'
Run the FastAPI Application with Uvicorn

bash
Copy code
uvicorn app:app --port 8000
