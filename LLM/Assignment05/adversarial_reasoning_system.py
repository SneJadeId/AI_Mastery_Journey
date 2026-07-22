import os
import json
import time
import requests
import urllib3

from pathlib import Path
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# ----------------------------------------------------
# Disable SSL warning
# ----------------------------------------------------

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

# ----------------------------------------------------
# Load .env
# ----------------------------------------------------

env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

BASE_URL = os.getenv("LLAMA_BASE_URL")

MODEL_A = os.getenv("MODEL_A")
MODEL_B = os.getenv("MODEL_B")

USERNAME = os.getenv("LLAMA_USERNAME")
PASSWORD = os.getenv("LLAMA_PASSWORD")

VERIFY_SSL = os.getenv(
    "LLAMA_VERIFY_SSL",
    "False"
).lower() == "true"

LOG_FILE = "interaction_log.txt"

# ----------------------------------------------------
# Logger
# ----------------------------------------------------

def log(title, text):

    with open(LOG_FILE, "a", encoding="utf-8") as f:

        f.write("\n")
        f.write("="*70 + "\n")
        f.write(title + "\n")
        f.write("="*70 + "\n")
        f.write(text + "\n")

# ----------------------------------------------------
# API Client with Retry
# ----------------------------------------------------

def call_model(model, system_prompt, user_prompt):

    url = f"{BASE_URL}/chat"

    payload = {

        "model": model,

        "messages": [

            {
                "role":"system",
                "content":system_prompt
            },

            {
                "role":"user",
                "content":user_prompt
            }

        ],

        "stream":False

    }

    retries = 3

    for attempt in range(retries):

        try:

            response = requests.post(

                url,

                json=payload,

                auth=HTTPBasicAuth(
                    USERNAME,
                    PASSWORD
                ),

                verify=VERIFY_SSL,

                timeout=120

            )

            response.raise_for_status()

            result = response.json()

            return result["message"]["content"]

        except Exception as e:

            print(f"Retry {attempt+1} :", e)

            time.sleep(2)

    return "API Failure"

# ----------------------------------------------------
# Validation
# ----------------------------------------------------

def validate(topic,response):

    if not response:
        return False

    if response == "API Failure":
        return False

    return True

# ----------------------------------------------------
# Prompt Builder
# ----------------------------------------------------

SYSTEM_PROMPT = """
You are an expert AI assistant.

Always provide logical reasoning.

Be concise and professional.
"""

# ----------------------------------------------------
# Main Workflow
# ----------------------------------------------------

def run(topic):

    # --------------------------
    # Model A
    # --------------------------

    prompt_a = f"""
Scenario

{topic}

Provide:

1. Proposed Solution

2. Reasoning

3. Benefits
"""

    response_a = call_model(

        MODEL_A,

        SYSTEM_PROMPT,

        prompt_a

    )

    log("MODEL A PROMPT",prompt_a)
    log("MODEL A RESPONSE",response_a)

    if not validate(topic,response_a):
        raise Exception("Invalid Model A Response")

    # --------------------------
    # Model B
    # --------------------------

    prompt_b = f"""
Scenario

{topic}

Model A Proposal

{response_a}

Identify:

- Weaknesses

- Risks

- Edge Cases

- Counter Arguments
"""

    response_b = call_model(

        MODEL_B,

        SYSTEM_PROMPT,

        prompt_b

    )

    log("MODEL B PROMPT",prompt_b)
    log("MODEL B RESPONSE",response_b)

    if not validate(topic,response_b):
        raise Exception("Invalid Model B Response")

    # --------------------------
    # Model A Revision
    # --------------------------

    prompt_a2 = f"""
Scenario

{topic}

Original Proposal

{response_a}

Critique

{response_b}

Revise or defend the proposal.

Mention improvements.
"""

    response_a2 = call_model(

        MODEL_A,

        SYSTEM_PROMPT,

        prompt_a2

    )

    log("MODEL A FINAL PROMPT",prompt_a2)
    log("MODEL A FINAL RESPONSE",response_a2)

    # --------------------------
    # Final Evaluation
    # --------------------------

    final_prompt = f"""
Scenario

{topic}

Proposal

{response_a2}

Remaining Risks

Summarize robustness and remaining risks
in 4 sentences.
"""

    evaluation = call_model(

        MODEL_A,

        SYSTEM_PROMPT,

        final_prompt

    )

    log("FINAL EVALUATION",evaluation)

    return {

        "original_input":topic,

        "model_a_initial_proposal":response_a,

        "model_b_critique":response_b,

        "model_a_revised_response":response_a2,

        "final_evaluation":evaluation

    }

# ----------------------------------------------------
# Main
# ----------------------------------------------------

def main():

    print("="*60)
    print("MULTI MODEL ADVERSARIAL REASONING SYSTEM")
    print("="*60)

    topic = input("\nEnter Scenario:\n\n")

    result = run(topic)

    print("\n")

    print(json.dumps(result,indent=4))

if __name__ == "__main__":

    main()