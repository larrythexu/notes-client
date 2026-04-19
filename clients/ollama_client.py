import requests


class OllamaClient:
    def __init__(self, model: str = "gemma4:e2b"):
        self.model = model
        self.base_url = "http://localhost:11434/api"

    def generate(self, prompt: str):
        res = requests.post(self.base_url + "/generate", json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })

        res.raise_for_status()
        return res.json()["response"]
