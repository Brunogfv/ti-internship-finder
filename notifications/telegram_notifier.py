import telebot
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def send_telegram_notification(jobs):
    message = "Novas vagas de estágio em TI:\n"
    for job in jobs[:5]:  # Limitar
        message += f"{job['titulo']} - {job['empresa']} - {job['link']}\n"
    bot.send_message(TELEGRAM_CHAT_ID, message)