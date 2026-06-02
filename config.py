import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent
DB_PATH = str(BASE_DIR / 'jobs.db')
CSV_PATH = str(BASE_DIR / 'jobs.csv')
LOG_PATH = str(BASE_DIR / 'logs' / 'system.log')

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_TO = os.getenv('EMAIL_TO')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
try:
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
except (ValueError, TypeError):
    SMTP_PORT = 587
