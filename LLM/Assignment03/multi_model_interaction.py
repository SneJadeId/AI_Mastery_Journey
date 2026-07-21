import os
import json
import requests
import urllib3
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

BASE_URL = os.getenv("LLAMA_BASE_URL")

# Two models
MODEL_A = os.getenv("MODEL_A")
MODEL_B = os.getenv("MODEL_B")

VERIFY_SSL = os.getenv("LLAMA_VERIFY_SSL", "False").lower() == "true"

USERNAME = os.getenv("LLAMA_USERNAME")
PASSWORD = os.getenv("LLAMA_PASSWORD")

LOG_FILE = "interaction_log.txt"


# ==========================================
# Logging
# ==========================================

def log(title, content):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("=" * 70 + "\n")
        f.write(title + "\n")
        f.write("=" * 70 + "\n")
        f.write(content)
        f.write("\n")


# ==========================================
# API Client
# ==========================================

def call_model(model_name, system_prompt, user_prompt):

    url = f"{BASE_URL}/chat"

    payload = {
        "model": model_name,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "stream": False
    }

    try:

        response = requests.post(
            url,
            json=payload,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            verify=VERIFY_SSL,
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        if "message" in result:
            return result["message"]["content"]

        elif "response" in result:
            return result["response"]

        else:
            return ""

    except Exception as e:

        return f"API Error: {e}"


# ==========================================
# Validation
# ==========================================

def validate_response(topic, response):

    if not response:
        return False

    if response.startswith("API Error"):
        return False

    # Simple relevance check
    words = topic.lower().split()

    for word in words:
        if word in response.lower():
            return True

    return True


# ==========================================
# Orchestration
# ==========================================

def run_discussion(topic):

    system_prompt = (
        "You are an intelligent AI assistant. "
        "Give detailed, professional responses."
    )

    # -----------------------------
    # Turn 1 (Model A)
    # -----------------------------

    prompt_a1 = f"""
Topic:
{topic}

Explain your position in detail.
"""

    response_a1 = call_model(
        MODEL_A,
        system_prompt,
        prompt_a1
    )

    log("MODEL A - PROMPT", prompt_a1)
    log("MODEL A - RESPONSE", response_a1)

    if not validate_response(topic, response_a1):
        raise Exception("Invalid response from Model A")

    # -----------------------------
    # Turn 2 (Model B)
    # -----------------------------

    prompt_b = f"""
Topic:

{topic}

Model A said:

{response_a1}

Critique, question or expand upon the above response.
"""

    response_b = call_model(
        MODEL_B,
        system_prompt,
        prompt_b
    )

    log("MODEL B - PROMPT", prompt_b)
    log("MODEL B - RESPONSE", response_b)

    if not validate_response(topic, response_b):
        raise Exception("Invalid response from Model B")

    # -----------------------------
    # Turn 3 (Model A)
    # -----------------------------

    prompt_a2 = f"""
Topic:

{topic}

Model B replied:

{response_b}

Respond to Model B.
"""

    response_a2 = call_model(
        MODEL_A,
        system_prompt,
        prompt_a2
    )

    log("MODEL A FINAL - PROMPT", prompt_a2)
    log("MODEL A FINAL - RESPONSE", response_a2)

    if not validate_response(topic, response_a2):
        raise Exception("Invalid final response")

    # -----------------------------
    # Final Conclusion
    # -----------------------------

    conclusion_prompt = f"""
Topic:
{topic}

Model A Initial Response:

{response_a1}

Model B Response:

{response_b}

Model A Final Reply:

{response_a2}

Write a short conclusion (3-4 sentences).
"""

    conclusion = call_model(
        MODEL_A,
        system_prompt,
        conclusion_prompt
    )

    log("CONCLUSION PROMPT", conclusion_prompt)
    log("CONCLUSION RESPONSE", conclusion)

    return {
        "topic": topic,
        "model_a_initial_response": response_a1,
        "model_b_response": response_b,
        "model_a_final_response": response_a2,
        "conclusion": conclusion
    }


# ==========================================
# Main
# ==========================================

def main():

    print("=" * 60)
    print("MULTI MODEL INTERACTION SYSTEM")
    print("=" * 60)

    topic = input("\nEnter Topic:\n\n")

    try:

        result = run_discussion(topic)

        print("\n")
        print(json.dumps(result, indent=4))

    except Exception as e:

        print("\nError:", e)


if __name__ == "__main__":
    main()