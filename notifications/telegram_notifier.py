from typing import Any, Optional
import telebot
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

_bot: Optional[telebot.TeleBot] = None


def _get_bot() -> Optional[telebot.TeleBot]:
    global _bot
    if _bot is None and TELEGRAM_TOKEN:
        _bot = telebot.TeleBot(TELEGRAM_TOKEN)
    return _bot


def send_telegram_notification(jobs: list[dict[str, Any]]) -> None:
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return
    bot = _get_bot()
    if not bot:
        return

    message = f"<b>Novas vagas de estágio em TI ({len(jobs)})</b>\n\n"
    for job in jobs[:10]:
        message += f"• <a href='{job['link']}'>{job['titulo']}</a> - {job['empresa']}\n"
    if len(jobs) > 10:
        message += f"\n...e mais {len(jobs) - 10} vagas"

    bot.send_message(TELEGRAM_CHAT_ID, message, parse_mode="HTML", disable_web_page_preview=True)
