import re

from company_llm import ask_llm

from stock_tools import (
    get_internal_stock_price,
    search_public_web
)

LOG_FILE = "interaction_log.txt"


def log(title, text):

    with open(LOG_FILE, "a", encoding="utf-8") as f:

        f.write("\n")
        f.write("=" * 60)
        f.write("\n")
        f.write(title)
        f.write("\n")
        f.write("=" * 60)
        f.write("\n")
        f.write(text)
        f.write("\n")


###########################################################

TOOLS = """
Available Tools

1.

get_internal_stock_price(ticker)

Description

Use FIRST whenever someone asks for a stock price.

This tool may fail due to database timeout.

------------------------------------------------

2.

search_public_web(query)

Description

Use ONLY if the internal database fails.

------------------------------------------------

Always think step by step.

Return ONLY

Thought:
Action:
Input:
"""

###########################################################


def ask_agent(query):

    prompt = f"""
{TOOLS}

User Question

{query}
"""

    return ask_llm(prompt)


###########################################################


def main():

    question = "What is the current stock price of Apple?"

    print("=" * 60)
    print("USER QUESTION")
    print("=" * 60)
    print(question)

    decision = ask_agent(question)

    print("\nThought Process\n")
    print(decision)

    ticker = "Apple"

    try:

        print("\nAction 1")
        print("Calling Internal Database...")

        result = get_internal_stock_price(ticker)

    except Exception as e:

        print("\nObservation")
        print(str(e))

        print("\nRecovering...")

        result = search_public_web(question)

    print("\nFinal Answer")
    print(result)

    log("Agent Decision", decision)
    log("Final Answer", result)


if __name__ == "__main__":
    main()