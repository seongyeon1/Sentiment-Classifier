from transformers import pipeline

class TextClassifier:
    def __init__(self):
        self.pipe = pipeline("text-classification", model="seongyeon1/klue-base-finetuned-nsmc")

    def predict(self, text: str):
        return self.pipe(text)
