import os
import json
import requests
import urllib3
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth


# Load environment variables
load_dotenv()

# Read values from .env
BASE_URL = os.getenv("LLAMA_BASE_URL")
MODEL = os.getenv("LLAMA_MODEL")
VERIFY_SSL = os.getenv("LLAMA_VERIFY_SSL", "False").lower() == "true"
USERNAME = os.getenv("LLAMA_USERNAME")
PASSWORD = os.getenv("LLAMA_PASSWORD")

print("========== Configuration ==========")
print("Base URL :", BASE_URL)
print("Model    :", MODEL)
print("SSL      :", VERIFY_SSL)
print("Username :", USERNAME)
print("===================================\n")

url = f"{BASE_URL}/chat"

payload = {
    "model": MODEL,
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        },
        {
            "role": "user",
            "content": "Say Hello in one sentence."
        }
    ],
    "stream": False
}

try:
    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        verify=VERIFY_SSL,
        timeout=120
    )

    print("Status Code:", response.status_code)
    print("\nResponse Headers:")
    print(response.headers)

    print("\nResponse Body:")
    print(response.text)

    if response.status_code == 200:
        print("\n✅ SUCCESS! Connected to the LLM API.")

        result = response.json()

        if "message" in result:
            print("\nAssistant Reply:")
            print(result["message"]["content"])
        elif "response" in result:
            print("\nAssistant Reply:")
            print(result["response"])
        else:
            print("\nResponse JSON:")
            print(json.dumps(result, indent=4))

    elif response.status_code == 401:
        print("\n❌ Authentication failed. Check username/password.")

    elif response.status_code == 403:
        print("\n❌ Forbidden. Make sure you're connected to the Jade VPN/corporate network.")

    else:
        print(f"\n❌ Unexpected status code: {response.status_code}")

except Exception as e:
    print("\nException:")
    print(e)