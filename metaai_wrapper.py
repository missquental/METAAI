import requests
import uuid
import time

META_ENDPOINT = "https://www.meta.ai/"

HEADERS_BASE = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*",
    "Origin": "https://www.meta.ai",
    "Referer": "https://www.meta.ai/",
}

def safe_json(r):
    try:
        return r.json()
    except Exception:
        return {
            "error": "Non-JSON response",
            "status_code": r.status_code,
            "raw": r.text[:500]
        }

class MetaAIWrapper:
    def __init__(self, cookie: str):
        self.headers = HEADERS_BASE.copy()
        self.headers["Cookie"] = cookie

    def chat(self, prompt: str):
        r = requests.get(
            META_ENDPOINT,
            headers=self.headers,
            timeout=20
        )

        data = safe_json(r)
        return data

    def generate_video(self, prompt: str):
        r = requests.get(
            META_ENDPOINT,
            headers=self.headers,
            timeout=20
        )

        return safe_json(r)
