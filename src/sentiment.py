from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np


MODEL_NAME = "ProsusAI/finbert"


class SentimentAnalyzer:
    def __init__(self):
        print("[MODEL] Loading FinBERT model... this takes time only once")
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        self.model.eval()

        self.id2label = {
            0: "negative",
            1: "neutral",
            2: "positive",
        }

    @torch.no_grad()
    def predict(self, text: str):
        inputs = self.tokenizer(
            text,
            truncation=True,
            padding=True,
            max_length=128,
            return_tensors="pt"
        )

        outputs = self.model(**inputs)
        probs = torch.softmax(outputs.logits, dim=-1).numpy()[0]

        label_id = int(np.argmax(probs))
        return self.id2label[label_id], float(probs[label_id])


if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    label, conf = analyzer.predict("Apple stock jumps after record sales")
    print(label, conf)
