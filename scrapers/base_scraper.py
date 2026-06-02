import logging
import re
from datetime import datetime, timedelta
from typing import Any, Optional, Callable
from core.playwright_helper import get_page


def _parse_date(text: str) -> Optional[str]:
    text = text.strip().lower()
    today = datetime.now()

    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', text)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"

    match = re.search(r'(\d{2})/(\d{2})/(\d{4})', text)
    if match:
        return f"{match.group(3)}-{match.group(2)}-{match.group(1)}"

    match = re.search(r'há\s*(\d+)\s*dias?', text)
    if match:
        days = int(match.group(1))
        return (today - timedelta(days=days)).strftime('%Y-%m-%d')

    match = re.search(r'há\s*(\d+)\s*horas?', text)
    if match:
        return today.strftime('%Y-%m-%d')

    return None


class BaseScraper:
    def __init__(self, name: str, url: str, card_selector: str,
                 title_selector: str, company_selector: str,
                 location_selector: str, link_from_card: bool = False,
                 link_selector: Optional[str] = None,
                 link_builder: Optional[Callable[[str], str]] = None,
                 card_selector_fallback: Optional[str] = None,
                 page_timeout: int = 30000, wait_timeout: int = 3000,
                 use_company_in_tipo: bool = False,
                 tipo_extra_selector: Optional[str] = None,
                 skip_if_no_title_and_company: bool = False,
                 date_selector: Optional[str] = None) -> None:
        self.name = name
        self.url = url
        self.card_selector = card_selector
        self.card_selector_fallback = card_selector_fallback
        self.title_selector = title_selector
        self.company_selector = company_selector
        self.location_selector = location_selector
        self.link_from_card = link_from_card
        self.link_selector = link_selector
        self.link_builder = link_builder or (lambda href: href or "")
        self.page_timeout = page_timeout
        self.wait_timeout = wait_timeout
        self.use_company_in_tipo = use_company_in_tipo
        self.tipo_extra_selector = tipo_extra_selector
        self.skip_if_no_title_and_company = skip_if_no_title_and_company
        self.date_selector = date_selector

    def _extract_date(self, card: Any) -> str:
        if not self.date_selector:
            return datetime.now().strftime('%Y-%m-%d')
        try:
            el = card.query_selector(self.date_selector)
            if el:
                text = el.inner_text().strip()
                parsed = _parse_date(text)
                if parsed:
                    return parsed
        except Exception:
            pass
        return datetime.now().strftime('%Y-%m-%d')

    def scrape(self, max_jobs: int = 15) -> list[dict[str, Any]]:
        jobs: list[dict[str, Any]] = []
        page = get_page()
        try:
            page.goto(self.url, timeout=self.page_timeout, wait_until="domcontentloaded")
            page.wait_for_timeout(self.wait_timeout)

            cards = page.query_selector_all(self.card_selector)
            if not cards and self.card_selector_fallback:
                cards = page.query_selector_all(self.card_selector_fallback)

            if not cards:
                logging.info(f"{self.name}: nenhum card encontrado")
                return jobs

            for card in cards[:max_jobs]:
                try:
                    if self.link_selector:
                        link_el = card.query_selector(self.link_selector)
                    elif self.link_from_card:
                        link_el = card
                    else:
                        link_el = card.query_selector(self.title_selector)
                    title_el = card.query_selector(self.title_selector)
                    company_el = card.query_selector(self.company_selector)
                    location_el = card.query_selector(self.location_selector)

                    title = title_el.inner_text().strip() if title_el else ""
                    company = company_el.inner_text().strip() if company_el else ""
                    location = location_el.inner_text().strip() if location_el else ""
                    href = link_el.get_attribute("href") if link_el else ""
                    link = self.link_builder(href)

                    text = title + " " + location
                    if self.use_company_in_tipo:
                        text += " " + company
                    if self.tipo_extra_selector:
                        extra_el = card.query_selector(self.tipo_extra_selector)
                        if extra_el:
                            text += " " + extra_el.inner_text()
                    text = text.lower()

                    if "remoto" in text:
                        tipo = "remoto"
                    elif "híbrido" in text or "hibrido" in text:
                        tipo = "híbrido"
                    else:
                        tipo = "presencial"

                    if self.skip_if_no_title_and_company:
                        if not title and not company:
                            continue
                    elif not title:
                        continue

                    jobs.append({
                        'titulo': title,
                        'empresa': company,
                        'localizacao': location,
                        'tipo': tipo,
                        'link': link,
                        'data_publicacao': self._extract_date(card),
                        'descricao_resumida': ''
                    })
                except Exception as e:
                    logging.warning(f"Erro ao extrair card {self.name}: {e}")
                    continue

        except Exception as e:
            logging.error(f"Erro no scraping {self.name}: {e}")

        return jobs
