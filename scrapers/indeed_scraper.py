from scrapers.base_scraper import BaseScraper


def _build_indeed_link(href):
    if not href:
        return ""
    if href.startswith("http"):
        return href
    return "https://br.indeed.com" + href


scraper = BaseScraper(
    name="Indeed",
    url="https://br.indeed.com/jobs?q=est%C3%A1gio+TI&l=",
    card_selector="div.job_seen_beacon, div.cardOutline, li.css-5lf1m8",
    title_selector="h2.jobTitle a, h2 a, a.jobtitle, h3.jobTitle a, .jcs-JobTitle",
    company_selector="span[data-testid='company-name']",
    location_selector="div[data-testid='text-location']",
    link_selector=".jcs-JobTitle",
    card_selector_fallback="div.jobsearch-SerpJobCard",
    link_builder=_build_indeed_link,
    wait_timeout=5000,
)


def scrape_indeed(max_jobs=15):
    return scraper.scrape(max_jobs)
