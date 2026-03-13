import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

def scrape_glassdoor():
    jobs = []
    url = "https://www.glassdoor.com.br/Vaga/est%C3%A1gio-ti-brasil-vagas-SRCH_KO0,10.htm"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        job_cards = soup.find_all('li', class_='react-job-listing')

        for card in job_cards[:10]:
            title = card.find('a', class_='jobLink').text.strip() if card.find('a', class_='jobLink') else ''
            company = card.find('div', class_='jobHeader').find('span').text.strip() if card.find('div', class_='jobHeader') else ''
            location = card.find('span', class_='loc').text.strip() if card.find('span', class_='loc') else ''
            link = "https://www.glassdoor.com.br" + card.find('a')['href'] if card.find('a') else ''
            jobs.append({
                'titulo': title,
                'empresa': company,
                'localizacao': location,
                'tipo': 'remoto' if 'remoto' in location.lower() else 'presencial',
                'link': link,
                'data_publicacao': datetime.now().strftime('%Y-%m-%d'),
                'descricao_resumida': ''
            })
            time.sleep(1)

    except Exception as e:
        print(f"Erro no scraping Glassdoor: {e}")

    return jobs