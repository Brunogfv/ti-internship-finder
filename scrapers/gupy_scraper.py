from scrapers.base_scraper import BaseScraper


scraper = BaseScraper(
    name="Gupy",
    url="https://portal.gupy.io/job-search/term=estagio",
    card_selector="a[href*='/job/']",
    title_selector="h3",
    company_selector="p",
    location_selector="span[data-testid='job-location']",
    link_from_card=True,
    date_selector="[data-testid='listing-card-footer']",
    wait_timeout=8000,
    use_company_in_tipo=True,
    tipo_extra_selector="[data-testid='listing-details']",
)


def scrape_gupy(max_jobs=15):
    return scraper.scrape(max_jobs)
