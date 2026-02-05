import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_news(topic="technology"):
    key = os.getenv("NEWS_API_KEY")
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={topic}&sortBy=publishedAt&pageSize=3&apiKey={key}"
    )
    res = requests.get(url).json()

    articles = []
    for a in res.get("articles", []):
        articles.append({
            "name": a["title"],
            "source": a["source"]["name"],
            "description": a["description"],
            "url": a["url"]
        })

    return articles