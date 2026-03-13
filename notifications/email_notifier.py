import smtplib
from email.mime.text import MIMEText
import os

try:
    EMAIL_FROM = os.getenv('EMAIL_FROM')
    EMAIL_TO = os.getenv('EMAIL_TO')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    if not EMAIL_FROM:
        from config import EMAIL_FROM, EMAIL_TO, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT
except ImportError:
    from config import EMAIL_FROM, EMAIL_TO, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

def send_daily_email(jobs):
    msg = MIMEText("Resumo diário de vagas: " + str(len(jobs)) + " novas.")
    msg['Subject'] = 'Vagas de Estágio TI'
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_PASSWORD)
    server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    server.quit()