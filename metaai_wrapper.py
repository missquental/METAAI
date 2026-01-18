import requests
import uuid
import time

META_ENDPOINT = "https://www.meta.ai/api/graphql/"

HEADERS_BASE = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Origin": "https://www.meta.ai",
    "Referer": "https://www.meta.ai/",
}

class MetaAIWrapper:
    def __init__(self, cookie: str):
        self.headers = HEADERS_BASE.copy()
        self.headers["Cookie"] = cookie

    # =========================
    # CHAT
    # =========================
    def chat(self, prompt: str) -> str:
        payload = {
            "prompt": prompt,
            "conversation_id": str(uuid.uuid4())
        }

        r = requests.post(
            META_ENDPOINT,
            headers=self.headers,
            json=payload,
            timeout=30
        )

        r.raise_for_status()
        data = r.json()

        return data.get("text", "Tidak ada response")

    # =========================
    # VIDEO GENERATION
    # =========================
    def generate_video(self, prompt: str):
        payload = {
            "prompt": prompt,
            "media_type": "video"
        }

        r = requests.post(
            META_ENDPOINT,
            headers=self.headers,
            json=payload,
            timeout=30
        )
        r.raise_for_status()
        data = r.json()

        return {
            "conversation_id": data.get("conversation_id"),
            "status": data.get("status", "processing")
        }

    def poll_video(self, conversation_id: str, wait=5, retries=6):
        for _ in range(retries):
            r = requests.get(
                META_ENDPOINT,
                headers=self.headers,
                params={"conversation_id": conversation_id},
                timeout=30
            )
            r.raise_for_status()
            data = r.json()

            urls = data.get("video_urls")
            if urls:
                return urls

            time.sleep(wait)

        return []
