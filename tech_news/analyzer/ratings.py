from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    return [
        category[0]
        for category in Counter(
            [news["category"] for news in find_news()]
        ).most_common(5)
    ]
