import re

from company_llm import ask_llm

from tools import (
    refund_order,
    cancel_subscription
)

############################################################
# Logging
############################################################

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


############################################################
# Agent
############################################################

TOOL_DESCRIPTIONS = """
Available Tools

refund_order(transaction_id)

Description:
Refunds a completed transaction.
Use only when user wants money back.

------------------------------------------------

cancel_subscription(email)

Description:
Stops future recurring subscription payments.
Use only when user wants to stop future billing.

------------------------------------------------

You must choose ONLY ONE tool.

Reply ONLY in this format.

Tool: tool_name
Input: parameter
Reason: one sentence

Do not write anything else.
"""


def decide_tool(user_query):

    prompt = f"""
{TOOL_DESCRIPTIONS}

User Request

{user_query}
"""

    reply = ask_llm(prompt)

    log("LLM Decision", reply)

    return reply


############################################################
# Execute Tool
############################################################

def execute(decision):

    tool_match = re.search(
        r"Tool:\s*(.*)",
        decision,
        re.IGNORECASE
    )

    input_match = re.search(
        r"Input:\s*(.*)",
        decision,
        re.IGNORECASE
    )

    if tool_match is None or input_match is None:
        return "Unable to understand tool selection."

    tool = tool_match.group(1).strip().lower()
    value = input_match.group(1).strip()

    if tool == "refund_order":

        return refund_order(value)

    elif tool == "cancel_subscription":

        return cancel_subscription(value)

    return "Unknown tool."


############################################################

def run(query):

    print("=" * 60)
    print("User Request")
    print("=" * 60)
    print(query)

    decision = decide_tool(query)

    print("\nAgent Decision\n")
    print(decision)

    result = execute(decision)

    print("\nTool Output\n")
    print(result)

    log("Final Result", result)


############################################################

if __name__ == "__main__":

    print("\nTEST CASE 1\n")

    run(
        "I don't want to use your software anymore. "
        "Stop charging john@email.com."
    )

    print("\n\n")

    print("TEST CASE 2\n")

    run(
        "My last charge of $50 on transaction ID TXN991 "
        "was a mistake. Give my money back."
    )