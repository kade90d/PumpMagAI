import requests
from app.config import NEWS_API_KEY

def fetch_news_articles(topic="AI", count=5):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response.get("articles", [])
    return [article["title"] + "\n" + article["description"] for article in articles[:count]]