from scrapers.base_scraper import BaseScraper


scraper = BaseScraper(
    name="Glassdoor",
    url="https://www.glassdoor.com.br/Vaga/est%C3%A1gio-ti-brasil-vagas-SRCH_KO0,10.htm",
    card_selector="li[data-test='jobListing']",
    title_selector="a[data-test='job-title'], a.job-title, a[aria-label*='vaga'], a[aria-label*='Vaga']",
    company_selector="[class*='EmployerProfile_compactEmployerName'], [class*='employerName']",
    location_selector="[data-test='emp-location']",
    link_selector="a[data-test='job-title']",
    card_selector_fallback="article[data-test^='job'], div.jobListing, li.react-job-listing",
    wait_timeout=5000,
    use_company_in_tipo=True,
    skip_if_no_title_and_company=True,
)


def scrape_glassdoor(max_jobs=15):
    return scraper.scrape(max_jobs)
