from scrapers.base_scraper import BaseScraper


scraper = BaseScraper(
    name="LinkedIn",
    url="https://www.linkedin.com/jobs/search/?keywords=est%C3%A1gio%20TI&location=Brasil&geoId=106057199",
    card_selector=".job-search-card",
    title_selector=".base-search-card__title",
    company_selector=".base-search-card__subtitle",
    location_selector=".job-search-card__location",
    link_selector=".base-card__full-link",
    date_selector=".base-search-card__metadata time",
    page_timeout=20000,
    wait_timeout=5000,
)


def scrape_linkedin(max_jobs=15):
    return scraper.scrape(max_jobs)
