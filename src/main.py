from datetime import datetime
from news_api import fetch_news
from sentiment import SentimentAnalyzer
from strategy import sentiment_to_signal
from storage import save_records


TICKERS = ["AAPL", "TSLA", "GOOGL"]


def run():
    analyzer = SentimentAnalyzer()
    records = []

    for ticker in TICKERS:
        print(f"[NEWS] Fetching headlines for {ticker}")
        articles = fetch_news(ticker)

        for item in articles:
            label, conf = analyzer.predict(item["title"])
            signal = sentiment_to_signal(label, conf)

            records.append({
                "timestamp": datetime.utcnow().isoformat(),
                "ticker": ticker,
                "title": item["title"],
                "sentiment": label,
                "confidence": conf,
                "signal": signal,
                "url": item["url"],
            })

    if records:
        df = save_records(records)
        print(f"[DONE] Saved {len(records)} rows. Total dataset: {len(df)}")
    else:
        print("[WARN] No news found")


if __name__ == "__main__":
    run()
