import schedule
import time
from main import main

def run_scheduler():
    schedule.every().day.at("09:00").do(main)
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    run_scheduler()