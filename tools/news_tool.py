import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&pageSize=3&apiKey={NEWS_API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        articles = []
        for a in data.get("articles", [])[:3]:
            articles.append({
                "name": a["title"],
                "source": a["source"]["name"],
                "description": a["description"],
                "url": a["url"]
            })

        return articles

    except Exception as e:
        return {"error": str(e)}