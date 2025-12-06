# 🧠 Stock News Sentiment Trader

An end-to-end **AI pipeline** that:
1. Fetches latest stock-related news headlines
2. Runs **FinBERT** (finance-specific BERT) for sentiment analysis
3. Converts sentiment into simple **BUY / SELL / HOLD** signals
4. Stores signals in a dataset
5. Visualizes everything in an interactive **Streamlit dashboard**

Built with a focus on **AIML + real-world APIs + deployment-readiness**.

---

## 🔍 Features

- ✅ Live news scraping via NewsAPI
- ✅ Transformer-based sentiment analysis (`ProsusAI/finbert`)
- ✅ Rule-based trading signal engine
- ✅ Persistent storage of signals (`data/signals.csv`)
- ✅ Streamlit dashboard:
  - Recent signals table
  - Signal distribution (BUY/SELL/HOLD)
  - Confidence trend over time

---

## 🏗 Tech Stack

- **Language:** Python 3.x  
- **NLP:** `transformers`, FinBERT (`ProsusAI/finbert`)  
- **Data:** `pandas`  
- **App:** `streamlit`  
- **Config:** `.env` + `python-dotenv`  
- **HTTP:** `requests`  

---

## 📦 Project Structure

```bash
stock-news-sentiment-trader/
├── src/
│   ├── news_api.py       # Fetches news from NewsAPI
│   ├── sentiment.py      # FinBERT sentiment model
│   ├── strategy.py       # Sentiment → BUY/SELL/HOLD logic
│   ├── storage.py        # Append signals to CSV
│   ├── main.py           # Orchestrates full pipeline
│   └── dashboard.py      # Streamlit dashboard
├── data/                 # Generated signals.csv (ignored in git)
├── requirements.txt
├── .env                  # API keys (NOT committed)
├── .gitignore
└── README.md

---

## 🚀 How to Run This Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Aditya1865/stock-news-sentiment-trader.git
cd stock-news-sentiment-trader

### 2️⃣ Create Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate     # macOS / Linux users
# venv\Scripts\activate      # Windows users

### 3️⃣ Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

### 4️⃣ Add Your API Key
NEWS_API_KEY=your_newsapi_key_here
NEWS_API_ENDPOINT=https://newsapi.org/v2/everything

Get your free NewsAPI key here: https://newsapi.org/register

##🧠 Run the AI Pipeline

This command fetches news → performs sentiment → generates signals:

python3 src/main.py


Output:

Logs in terminal

Creates/updates data/signals.csv

##📊 Launch the Dashboard

Visualize signals interactively on a local web app:

streamlit run src/dashboard.py


Then open the link shown in the terminal (usually):

http://localhost:8501


Dashboard Features:

Sentiment confidence chart

Latest BUY/SELL/HOLD signals

Filter by stock ticker

##🧪 Optional Debug Commands

Test news fetching only:

python3 src/news_api.py


Test sentiment model only:

python3 src/sentiment.py
