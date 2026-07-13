import requests
import json

# ==========================================
# Company LLM Configuration
# ==========================================

BASE_URL = "https://aimodels.jadeglobal.com:8082/ollama/api"
MODEL = "llama3.1:8b"

# ==========================================
# Function to Query LLM
# ==========================================

def query_llm(prompt):

    url = f"{BASE_URL}/generate"

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            url,
            json=payload,
            verify=False,
            timeout=60
        )

        response.raise_for_status()

        return response.json()["response"]

    except requests.exceptions.RequestException as e:

        print("API Error:", e)
        return None


# ==========================================
# Prompt Builder
# ==========================================

def build_prompt(article):

    prompt = f"""
You are an Article Analysis Assistant.

Analyze the article below.

Return ONLY valid JSON.

The JSON must have exactly these fields:

{{
    "summary": "",
    "important_points": [],
    "key_themes": [],
    "target_audience": ""
}}

Rules:

1. Summary must be at most 150 words.
2. important_points must contain between 5 and 10 points.
3. key_themes must contain between 3 and 5 short phrases.
4. target_audience should be one short sentence.
5. Do NOT include markdown.
6. Do NOT include explanations.
7. Do NOT return anything outside the JSON object.

Article:

{article}
"""

    return prompt


# ==========================================
# Validate JSON
# ==========================================

def validate_response(response):

    try:

        data = json.loads(response)

    except json.JSONDecodeError:

        print("Invalid JSON received.")
        return None

    required_fields = [
        "summary",
        "important_points",
        "key_themes",
        "target_audience"
    ]

    for field in required_fields:

        if field not in data:
            print(f"Missing field: {field}")
            return None

    if not isinstance(data["important_points"], list):
        print("important_points should be a list.")
        return None

    if not isinstance(data["key_themes"], list):
        print("key_themes should be a list.")
        return None

    if len(data["important_points"]) < 5 or len(data["important_points"]) > 10:
        print("important_points should contain 5-10 items.")
        return None

    if len(data["key_themes"]) < 3 or len(data["key_themes"]) > 5:
        print("key_themes should contain 3-5 items.")
        return None

    return data


# ==========================================
# Main Program
# ==========================================

article = input("Enter Article:\n\n")

prompt = build_prompt(article)

response = query_llm(prompt)

if response:

    result = validate_response(response)

    if result:

        print("\nAnalysis Successful\n")

        print(json.dumps(result, indent=4))

    else:

        print("\nResponse validation failed.")

else:

    print("\nCould not connect to the API.")