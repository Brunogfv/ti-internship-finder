import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

def scrape_linkedin():
    jobs = []
    url = "https://www.linkedin.com/jobs/search/?keywords=est%C3%A1gio%20TI&location=Brasil"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        job_cards = soup.find_all('div', class_='job-search-card')

        for card in job_cards[:10]:  # Limitar para teste
            title = card.find('h3').text.strip() if card.find('h3') else ''
            company = card.find('h4').text.strip() if card.find('h4') else ''
            location = card.find('span', class_='job-search-card__location').text.strip() if card.find('span', class_='job-search-card__location') else ''
            link = card.find('a')['href'] if card.find('a') else ''
            # Outros campos podem precisar de mais parsing
            jobs.append({
                'titulo': title,
                'empresa': company,
                'localizacao': location,
                'tipo': 'remoto' if 'remoto' in location.lower() else 'presencial',
                'link': link,
                'data_publicacao': datetime.now().strftime('%Y-%m-%d'),
                'descricao_resumida': ''
            })
            time.sleep(1)  # Delay para evitar bloqueio

    except Exception as e:
        print(f"Erro no scraping LinkedIn: {e}")

    return jobs