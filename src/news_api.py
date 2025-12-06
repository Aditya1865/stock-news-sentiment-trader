import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
ENDPOINT = os.getenv("NEWS_API_ENDPOINT", "https://newsapi.org/v2/everything")


def fetch_news(query: str = "stock market", page_size: int = 20):
    if not API_KEY:
        raise ValueError("NEWS_API_KEY not set in .env")

    from_date = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")

    params = {
        "q": query,
        "from": from_date,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": page_size,
        "apiKey": API_KEY,
    }

    resp = requests.get(ENDPOINT, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    articles = data.get("articles", [])
    cleaned = [
        {
            "source": a.get("source", {}).get("name"),
            "title": a.get("title"),
            "description": a.get("description"),
            "url": a.get("url"),
            "published_at": a.get("publishedAt"),
        }
        for a in articles
        if a.get("title")
    ]
    return cleaned


if __name__ == "__main__":
    news = fetch_news("AAPL")
    for n in news[:5]:
        print(n["published_at"], "-", n["title"])
