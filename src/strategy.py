from typing import Literal

Signal = Literal["BUY", "SELL", "HOLD"]


def sentiment_to_signal(label: str, confidence: float) -> Signal:
    label = label.lower()

    if label == "positive" and confidence >= 0.6:
        return "BUY"
    if label == "negative" and confidence >= 0.6:
        return "SELL"

    return "HOLD"
