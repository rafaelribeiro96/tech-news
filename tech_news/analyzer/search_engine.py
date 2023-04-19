from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    response = []
    for new in search_news({"title": {"$regex": title, "$options": "i"}}):
        response.append((new["title"], new["url"]))
    return response


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
