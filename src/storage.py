import os
import pandas as pd
from datetime import datetime

DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "signals.csv")


def ensure_data_folder():
    os.makedirs(DATA_DIR, exist_ok=True)


def save_records(records: list):
    ensure_data_folder()
    df_new = pd.DataFrame(records)

    if os.path.exists(FILE_PATH):
        df_old = pd.read_csv(FILE_PATH)
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = df_new

    df.to_csv(FILE_PATH, index=False)
    return df


if __name__ == "__main__":
    test = [{
        "timestamp": datetime.utcnow().isoformat(),
        "ticker": "AAPL",
        "title": "Fake test news",
        "sentiment": "positive",
        "confidence": 0.91,
        "signal": "BUY",
        "url": "https://example.com"
    }]
    print(save_records(test))
