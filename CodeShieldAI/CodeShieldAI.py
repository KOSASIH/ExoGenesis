import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


class CodeShieldAI:
    def __init__(self, model_name, tokenizer_name):
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    def detect_threat(self, code_snippet):
        inputs = self.tokenizer(code_snippet, return_tensors="pt")
        outputs = self.model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=-1)
        return probabilities.argmax().item()


# Example usage
code_shield_ai = CodeShieldAI("microsoft/codebert-base", "microsoft/codebert-base")
code_snippet = "def add(a, b): return a + b"
threat_detected = code_shield_ai.detect_threat(code_snippet)

if threat_detected == 0:
    print("No threat detected.")
elif threat_detected == 1:
    print("Threat detected.")
else:
    print("Error in threat detection.")
