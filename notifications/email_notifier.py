import smtplib
import ssl
from typing import Any
from email.mime.text import MIMEText
from config import EMAIL_FROM, EMAIL_TO, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT


def send_daily_email(jobs: list[dict[str, Any]]) -> None:
    if not EMAIL_FROM or not EMAIL_PASSWORD:
        return
    body = "Resumo diário de vagas:\n\n"
    for job in jobs:
        body += f"{job['titulo']} - {job['empresa']}\n{job['link']}\n\n"
    msg = MIMEText(body)
    msg['Subject'] = f'Vagas de Estágio TI - {len(jobs)} novas'
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
