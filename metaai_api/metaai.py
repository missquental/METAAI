import requests
import json
from .utils import build_headers, extract_video_urls

class MetaAI:
    def __init__(self, cookies: dict):
        self.cookies = cookies
        self.headers = build_headers()

    def prompt(self, text, stream=False):
        # SIMPLIFIED contoh
        return {
            "message": f"(Dummy response) {text}"
        }

    def generate_video(self, prompt):
        # SIMPLIFIED contoh
        return {
            "success": True,
            "conversation_id": "dummy_id",
            "video_urls": []
        }
