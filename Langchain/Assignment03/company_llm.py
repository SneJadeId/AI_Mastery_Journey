import os
import requests
import urllib3

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

load_dotenv()

BASE_URL = os.getenv("LLAMA_BASE_URL")
MODEL = os.getenv("LLAMA_MODEL")
VERIFY_SSL = os.getenv("LLAMA_VERIFY_SSL", "False").lower() == "true"
USERNAME = os.getenv("LLAMA_USERNAME")
PASSWORD = os.getenv("LLAMA_PASSWORD")


def ask_llm(prompt: str):

    url = f"{BASE_URL}/chat"

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    response = requests.post(
        url,
        json=payload,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        verify=VERIFY_SSL,
        timeout=120
    )

    response.raise_for_status()

    return response.json()["message"]["content"]