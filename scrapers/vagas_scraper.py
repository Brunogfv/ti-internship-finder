from scrapers.base_scraper import BaseScraper


def _build_vagas_link(href):
    if not href:
        return ""
    if href.startswith("http"):
        return href
    return "https://www.vagas.com.br" + href


scraper = BaseScraper(
    name="Vagas.com",
    url="https://www.vagas.com.br/vagas-de-estagio-em-ti",
    card_selector="li.vaga, div.c-vaga, article[data-id]",
    title_selector="a.linkVaga, h2 a, a[class*='cargo'], a[class*='Cargo']",
    company_selector="span.emprVaga, span[class*='empresa'], span[class*='Empresa']",
    location_selector="span.local, span[class*='local'], span[class*='Local']",
    card_selector_fallback="li[class*='vaga'], div[class*='vaga']",
    link_builder=_build_vagas_link,
    wait_timeout=4000,
    use_company_in_tipo=True,
)


def scrape_vagas(max_jobs=15):
    return scraper.scrape(max_jobs)
