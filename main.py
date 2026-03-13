import logging
from scrapers.linkedin_scraper import scrape_linkedin
from scrapers.indeed_scraper import scrape_indeed
from scrapers.glassdoor_scraper import scrape_glassdoor
# from scrapers.vagas_scraper import scrape_vagas
# from scrapers.gupy_scraper import scrape_gupy
from core.job_filter import filter_jobs
from core.job_deduplicator import deduplicate_jobs
from core.job_database import save_jobs_to_db, export_to_csv
from notifications.telegram_notifier import send_telegram_notification
from notifications.email_notifier import send_daily_email
from datetime import datetime

logging.basicConfig(filename='logs/system.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def get_mock_jobs():
    return [
        {
            'titulo': 'Estágio em Desenvolvimento Python',
            'empresa': 'Empresa Exemplo',
            'localizacao': 'São Paulo, SP',
            'tipo': 'remoto',
            'link': 'https://example.com/job1',
            'data_publicacao': '2026-03-13',
            'descricao_resumida': 'Vaga para estágio em Python'
        },
        {
            'titulo': 'Estágio Backend Java',
            'empresa': 'Tech Corp',
            'localizacao': 'Rio de Janeiro, RJ',
            'tipo': 'híbrido',
            'link': 'https://example.com/job2',
            'data_publicacao': '2026-03-13',
            'descricao_resumida': 'Desenvolvimento backend'
        }
    ]

def main():
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}   TI Internship Finder - Busca de Vagas{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.ENDC}\n")
    
    logging.info("Iniciando busca de vagas")
    print(f"{Colors.YELLOW}⏳ Iniciando busca...{Colors.ENDC}\n")
    
    all_jobs = []

    # Scraping
    print(f"{Colors.BLUE}🔍 Scraping de vagas...{Colors.ENDC}")
    try:
        linkedin_jobs = scrape_linkedin()
        all_jobs.extend(linkedin_jobs)
        print(f"  ✓ LinkedIn: {len(linkedin_jobs)} vagas")
    except Exception as e:
        logging.error(f"Erro LinkedIn: {e}")
        print(f"  ✗ LinkedIn: Erro")
    
    try:
        indeed_jobs = scrape_indeed()
        all_jobs.extend(indeed_jobs)
        print(f"  ✓ Indeed: {len(indeed_jobs)} vagas")
    except Exception as e:
        logging.error(f"Erro Indeed: {e}")
        print(f"  ✗ Indeed: Erro")
    
    try:
        glassdoor_jobs = scrape_glassdoor()
        all_jobs.extend(glassdoor_jobs)
        print(f"  ✓ Glassdoor: {len(glassdoor_jobs)} vagas")
    except Exception as e:
        logging.error(f"Erro Glassdoor: {e}")
        print(f"  ✗ Glassdoor: Erro")

    # Se nenhum job encontrado, usar mock
    if not all_jobs:
        logging.info("Usando dados mock para teste")
        all_jobs = get_mock_jobs()
        print(f"{Colors.YELLOW}⚠️  Usando dados de teste para demonstração{Colors.ENDC}\n")
    else:
        print(f"{Colors.GREEN}✓ Encontradas {len(all_jobs)} vagas reais{Colors.ENDC}\n")

    # Filtragem
    from os import getenv
    debug_keep_all = getenv('DEBUG_KEEP_ALL', '0').lower() in ('1', 'true', 'yes')

    if debug_keep_all:
        print(f"{Colors.WARNING}⚠️  DEBUG_KEEP_ALL habilitado: pulando filtro. Todas as vagas serão mantidas.{Colors.ENDC}\n")
        filtered_jobs = all_jobs
    else:
        print(f"{Colors.BLUE}🔎 Filtrando vagas...{Colors.ENDC}")
        filtered_jobs = filter_jobs(all_jobs)
        print(f"  ✓ {len(filtered_jobs)} vagas após filtros\n")

    # Deduplicação
    print(f"{Colors.BLUE}🔄 Removendo duplicatas...{Colors.ENDC}")
    unique_jobs = deduplicate_jobs(filtered_jobs)
    print(f"  ✓ {len(unique_jobs)} vagas únicas\n")

    # Salvar no DB
    print(f"{Colors.BLUE}💾 Salvando no banco de dados...{Colors.ENDC}")
    new_jobs = save_jobs_to_db(unique_jobs)
    print(f"  ✓ {len(new_jobs)} novas vagas salvas\n")

    # Notificações
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

    # Export opcional
    export_to_csv(unique_jobs)
    print(f"{Colors.GREEN}✓ Arquivos atualizados:{Colors.ENDC}")
    print(f"  • {Colors.BOLD}jobs.csv{Colors.ENDC} - Arquivo Excel")
    print(f"  • {Colors.BOLD}jobs.db{Colors.ENDC} - Banco de dados")
    print(f"  • {Colors.BOLD}logs/system.log{Colors.ENDC} - Histórico\n")

    logging.info(f"Busca concluída. {len(new_jobs)} novas vagas encontradas.")
    print(f"{Colors.BOLD}{Colors.GREEN}✓ Busca concluída com sucesso!{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.ENDC}\n")

if __name__ == "__main__":
    main()