import requests
import json

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434", model="qwen2.5"):
        self.base_url = base_url
        self.model = model

    def chat(self, messages, tools=None):
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "tools": tools or []
        }
        resp = requests.post(f"{self.base_url}/api/chat", json=payload)
        return resp.json()["message"]