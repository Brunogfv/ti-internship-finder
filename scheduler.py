import logging
import signal
import sys
import time
import os
import schedule
from config import LOG_PATH

os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from main import main


def run_scheduler() -> None:
    logging.info("Agendador iniciado. Execução diária às 09:00.")
    schedule.every().day.at("09:00").do(main)

    def graceful_shutdown(signum, frame):
        logging.info("Agendador encerrado pelo usuário.")
        print("\nAgendador encerrado.")
        sys.exit(0)

    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)

    while True:
        try:
            schedule.run_pending()
            time.sleep(60)
        except Exception as e:
            logging.error(f"Erro no agendador: {e}")
            time.sleep(60)


if __name__ == "__main__":
    run_scheduler()
