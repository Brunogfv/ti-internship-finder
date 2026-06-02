import logging
import os
import sys
import json
from datetime import datetime
from typing import Any
from config import LOG_PATH, BASE_DIR
from core.colors import Colors
from core.job_database import create_db, save_jobs_to_db, export_to_csv
from core.job_filter import filter_jobs
from core.job_deduplicator import deduplicate_jobs
from core.playwright_helper import stop_browser
from notifications.telegram_notifier import send_telegram_notification
from notifications.email_notifier import send_daily_email
from scrapers.linkedin_scraper import scrape_linkedin
from scrapers.indeed_scraper import scrape_indeed
from scrapers.glassdoor_scraper import scrape_glassdoor
from scrapers.vagas_scraper import scrape_vagas
from scrapers.gupy_scraper import scrape_gupy

STATUS_PATH = BASE_DIR / 'last_run.json'

os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except (AttributeError, OSError):
    pass

create_db()


def _save_last_run(count: int) -> None:
    try:
        with open(STATUS_PATH, 'w') as f:
            json.dump({'ultima_execucao': datetime.now().isoformat(), 'novas_vagas': count}, f)
    except Exception:
        pass


def _run_scraper(name: str, scrape_fn: Any) -> list[dict[str, Any]]:
    try:
        jobs = scrape_fn()
        print(f"  ✓ {name}: {len(jobs)} vagas")
        return jobs
    except Exception as e:
        logging.error(f"Erro {name}: {e}")
        print(f"  ✗ {name}: Erro")
        return []


def main() -> None:
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}   TI Internship Finder - Busca de Vagas{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.ENDC}\n")

    logging.info("Iniciando busca de vagas")
    print(f"{Colors.YELLOW}⏳ Iniciando busca...{Colors.ENDC}\n")

    scrapers = [
        ("LinkedIn", scrape_linkedin),
        ("Indeed", scrape_indeed),
        ("Glassdoor", scrape_glassdoor),
        ("Vagas.com", scrape_vagas),
        ("Gupy", scrape_gupy),
    ]

    print(f"{Colors.BLUE}🔍 Scraping de vagas...{Colors.ENDC}")
    all_jobs: list[dict[str, Any]] = []
    for name, fn in scrapers:
        all_jobs.extend(_run_scraper(name, fn))

    if not all_jobs:
        logging.warning("Nenhuma vaga encontrada em nenhum scraper")
        print(f"{Colors.YELLOW}⚠️  Nenhuma vaga encontrada{Colors.ENDC}\n")
        return

    print(f"{Colors.GREEN}✓ Encontradas {len(all_jobs)} vagas{Colors.ENDC}\n")

    debug_keep_all = os.getenv('DEBUG_KEEP_ALL', '0').lower() in ('1', 'true', 'yes')

    if debug_keep_all:
        print(f"{Colors.WARNING}⚠️  DEBUG_KEEP_ALL habilitado: pulando filtro. Todas as vagas serão mantidas.{Colors.ENDC}\n")
        filtered_jobs = all_jobs
    else:
        print(f"{Colors.BLUE}🔎 Filtrando vagas...{Colors.ENDC}")
        filtered_jobs = filter_jobs(all_jobs)
        print(f"  ✓ {len(filtered_jobs)} vagas após filtros\n")

    print(f"{Colors.BLUE}🔄 Removendo duplicatas...{Colors.ENDC}")
    unique_jobs = deduplicate_jobs(filtered_jobs)
    print(f"  ✓ {len(unique_jobs)} vagas únicas\n")

    print(f"{Colors.BLUE}💾 Salvando no banco de dados...{Colors.ENDC}")
    new_jobs = save_jobs_to_db(unique_jobs)
    print(f"  ✓ {len(new_jobs)} novas vagas salvas\n")

    if new_jobs:
        print(f"{Colors.BLUE}📤 Enviando notificações...{Colors.ENDC}")
        try:
            send_telegram_notification(new_jobs)
            print(f"  ✓ Telegram: Notificações enviadas")
        except Exception as e:
            logging.error(f"Erro ao enviar Telegram: {e}")
            print(f"  ✗ Telegram: Erro")

        try:
            send_daily_email(new_jobs)
            print(f"  ✓ Email: Notificações enviadas")
        except Exception as e:
            logging.error(f"Erro ao enviar Email: {e}")
            print(f"  ✗ Email: Erro")
        print()

    export_to_csv(unique_jobs)
    print(f"{Colors.GREEN}✓ Arquivos atualizados:{Colors.ENDC}")
    print(f"  • {Colors.BOLD}jobs.csv{Colors.ENDC} - Arquivo Excel")
    print(f"  • {Colors.BOLD}jobs.db{Colors.ENDC} - Banco de dados")
    print(f"  • {Colors.BOLD}logs/system.log{Colors.ENDC} - Histórico\n")

    stop_browser()
    logging.info(f"Busca concluída. {len(new_jobs)} novas vagas encontradas.")
    _save_last_run(len(new_jobs))
    print(f"{Colors.BOLD}{Colors.GREEN}✓ Busca concluída com sucesso!{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.ENDC}\n")


if __name__ == "__main__":
    main()
