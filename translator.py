from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

class EN2GE:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-de").to(DEVICE)
        
    def translate(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt")
        inputs = {x: y.to(DEVICE) for x, y in inputs.items()}
        output = self.model.generate(**inputs)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)