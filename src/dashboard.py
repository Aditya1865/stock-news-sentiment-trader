import os
import pandas as pd
import streamlit as st

FILE_PATH = "data/signals.csv"


def load_data():
    if not os.path.exists(FILE_PATH):
        return pd.DataFrame()
    return pd.read_csv(FILE_PATH)


def main():
    st.title("📈 Stock Sentiment Trading Dashboard")

    df = load_data()
    if df.empty:
        st.warning("Run the pipeline first: python3 src/main.py")
        return

    tickers = sorted(df["ticker"].unique())
    ticker = st.sidebar.selectbox("Choose Stock", tickers)

    data = df[df["ticker"] == ticker]

    st.subheader(f"Latest Signals for {ticker}")
    st.dataframe(data.tail(25))

    st.subheader("Signal Stats")
    st.bar_chart(data["signal"].value_counts())

    st.subheader("Confidence Over Time")
    st.line_chart(data["confidence"])

    st.caption("Generated using FinBERT sentiment model")


if __name__ == "__main__":
    main()
