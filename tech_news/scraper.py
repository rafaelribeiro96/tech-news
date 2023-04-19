import requests
import time
import parsel
from tech_news.database import create_news
# Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url,
            timeout=3,
            headers={"User-Agent": "Fake User-Agent"}
        )
        if response.status_code == 200:
            return response.text
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = parsel.Selector(html_content)
    links = selector.css('a.cs-overlay-link::attr(href)').getall()
    return links

# Requisito 3


def scrape_next_page_link(html_content):
    selector = parsel.Selector(text=html_content)
    next_page = selector.css(".next.page-numbers::attr(href)").get()
    return next_page

# Requisito 4


def scrape_news(html_content):
    selector = parsel.Selector(html_content)
    return {
        'url': selector.css('link[rel=canonical]::attr(href)').get(),
        'title': selector.css('h1.entry-title::text').get().strip(),
        'timestamp': selector.css('li.meta-date::text').get(),
        'writer': selector.css('a.url.fn::text').get(),
        'reading_time': int(
            selector.css('li.meta-reading-time::text').get().split(" ")[0]
        ),
        'summary': selector.css(".entry-content p")
        .xpath("string()").get().strip(),
        'category': selector.css('.meta-category .label::text').get(),
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    response = []

    while len(response) < amount:
        page = fetch(url)
        links = scrape_updates(page)
        for link in links:
            if len(response) < amount:
                news = scrape_news(fetch(link))
                response.append(news)
        url = scrape_next_page_link(page)
        if not url:
            break
    create_news(response)
    return response
