from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    response = []
    for new in search_news({"title": {"$regex": title, "$options": "i"}}):
        response.append((new["title"], new["url"]))
    return response


# Requisito 8
def search_by_date(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        response = []
        for new in search_news({"timestamp": {"$eq": date}}):
            response.append((new["title"], new["url"]))
        return response
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
