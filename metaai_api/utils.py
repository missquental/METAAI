import requests
import json
import re

def build_headers():
    return {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }

def extract_video_urls(response_text):
    return re.findall(r'https://[^"\']+\.mp4', response_text)
