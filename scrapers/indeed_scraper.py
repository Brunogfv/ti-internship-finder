import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

def scrape_indeed():
    jobs = []
    url = "https://br.indeed.com/jobs?q=est%C3%A1gio+TI&l="
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        job_cards = soup.find_all('div', class_='job_seen_beacon')

        for card in job_cards[:10]:
            title = card.find('h2').text.strip() if card.find('h2') else ''
            company = card.find('span', class_='companyName').text.strip() if card.find('span', class_='companyName') else ''
            location = card.find('div', class_='companyLocation').text.strip() if card.find('div', class_='companyLocation') else ''
            link = "https://br.indeed.com" + card.find('a')['href'] if card.find('a') else ''
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
        print(f"Erro no scraping Indeed: {e}")

    return jobs