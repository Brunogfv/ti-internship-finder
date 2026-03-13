import os
import time
import subprocess
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}   TI Internship Finder - Monitor de Status{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.ENDC}")
    print()

def get_job_count():
    import sqlite3
    try:
        conn = sqlite3.connect('jobs.db')
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM jobs")
        count = c.fetchone()[0]
        conn.close()
        return count
    except:
        return 0

def get_csv_size():
    try:
        return os.path.getsize('jobs.csv')
    except:
        return 0

def tail_log(filename, lines=15):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.readlines()[-lines:]
    except:
        return []

def print_stats():
    jobs = get_job_count()
    csv_size = get_csv_size()
    
    print(f"{Colors.CYAN}{Colors.BOLD}📊 ESTATÍSTICAS ATUAIS:{Colors.ENDC}")
    print(f"  • Total de vagas no banco: {Colors.GREEN}{jobs}{Colors.ENDC}")
    print(f"  • Tamanho do CSV: {Colors.GREEN}{csv_size} bytes{Colors.ENDC}")
    print(f"  • Banco de dados: {Colors.GREEN}jobs.db{Colors.ENDC}")
    print(f"  • Arquivo CSV: {Colors.GREEN}jobs.csv{Colors.ENDC}")
    print()

def print_logs():
    print(f"{Colors.CYAN}{Colors.BOLD}📋 ÚLTIMOS LOGS (últimas 15 linhas):{Colors.ENDC}")
    print(f"{Colors.BLUE}{'-'*60}{Colors.ENDC}")
    
    logs = tail_log('logs/system.log')
    
    if not logs:
        print(f"{Colors.WARNING}Nenhum log encontrado ainda{Colors.ENDC}")
    else:
        for log in logs:
            line = log.strip()
            
            if 'INFO' in line:
                print(f"{Colors.GREEN}✓{Colors.ENDC} {line}")
            elif 'ERROR' in line:
                print(f"{Colors.FAIL}✗{Colors.ENDC} {line}")
            elif 'WARNING' in line:
                print(f"{Colors.WARNING}⚠{Colors.ENDC} {line}")
            else:
                print(f"  {line}")
    
    print(f"{Colors.BLUE}{'-'*60}{Colors.ENDC}")
    print()

def print_menu():
    print(f"{Colors.CYAN}{Colors.BOLD}⚙️  OPÇÕES:{Colors.ENDC}")
    print(f"  {Colors.BOLD}R{Colors.ENDC} - Rodar busca manual (main.py)")
    print(f"  {Colors.BOLD}S{Colors.ENDC} - Iniciar agendador (scheduler.py)")
    print(f"  {Colors.BOLD}A{Colors.ENDC} - Abrir API (api_start.bat)")
    print(f"  {Colors.BOLD}L{Colors.ENDC} - Limpar logs")
    print(f"  {Colors.BOLD}C{Colors.ENDC} - Config (abrir config.py)")
    print(f"  {Colors.BOLD}Q{Colors.ENDC} - Sair")
    print()

def main():
    while True:
        clear_screen()
        print_header()
        print_stats()
        print_logs()
        print_menu()
        
        print(f"{Colors.BOLD}Hora atual: {datetime.now().strftime('%H:%M:%S')}{Colors.ENDC}")
        print(f"{Colors.WARNING}Atualizando automaticamente...{Colors.ENDC}")
        
        try:
            # Aguardar input com timeout de 10 segundos
            import select
            import sys
            
            if os.name == 'nt':  # Windows
                # Abordagem simples para Windows
                choice = input(f"\n{Colors.BOLD}Digite uma opção: {Colors.ENDC}").upper()
            else:
                choice = ''
            
            if choice == 'R':
                print(f"\n{Colors.BOLD}{Colors.CYAN}Executando busca manual...{Colors.ENDC}")
                subprocess.run(['python', 'main.py'])
                time.sleep(2)
            
            elif choice == 'S':
                print(f"\n{Colors.BOLD}{Colors.CYAN}Iniciando agendador...{Colors.ENDC}")
                subprocess.run(['python', 'scheduler.py'])
            
            elif choice == 'A':
                print(f"\n{Colors.BOLD}{Colors.CYAN}Iniciando API...{Colors.ENDC}")
                subprocess.run(['agendador.bat'])
            
            elif choice == 'L':
                with open('logs/system.log', 'w') as f:
                    f.write('')
                print(f"{Colors.GREEN}✓ Logs limpos!{Colors.ENDC}")
                time.sleep(2)
            
            elif choice == 'C':
                print(f"\n{Colors.BOLD}{Colors.CYAN}Abrindo config.py...{Colors.ENDC}")
                os.system('notepad config.py')
            
            elif choice == 'Q':
                print(f"\n{Colors.BOLD}{Colors.GREEN}Até logo!{Colors.ENDC}")
                break
            
            else:
                time.sleep(5)  # Aguardar 5 segundos se não digitou nada
        
        except KeyboardInterrupt:
            print(f"\n{Colors.BOLD}{Colors.GREEN}Até logo!{Colors.ENDC}")
            break
        except Exception as e:
            time.sleep(5)

if __name__ == '__main__':
    main()