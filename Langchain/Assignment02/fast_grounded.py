from company_llm import CompanyLLM

############################################################
# Cache Dictionary
############################################################

query_cache = {}

############################################################
# Load Knowledge Base
############################################################

with open(
    "knowledge_base.txt",
    "r",
    encoding="utf-8"
) as f:

    knowledge = f.read()

############################################################
# LLM
############################################################

llm = CompanyLLM()

############################################################
# Grounded QA Function
############################################################

def ask_question(question):

    # -----------------------------
    # Check Cache
    # -----------------------------

    if question in query_cache:

        print("\nReturned from Cache\n")

        print(query_cache[question])

        return

    # -----------------------------
    # Build Prompt
    # -----------------------------

    prompt = f"""

You are a helpful AI assistant.

Use ONLY the context below.

If the answer cannot be found inside the context,
reply EXACTLY with

I do not have enough information.

Do not use your own knowledge.

Context:

{knowledge}

Question:

{question}

"""

    # -----------------------------
    # Call LLM
    # -----------------------------

    answer = llm.invoke(prompt)

    # -----------------------------
    # Save to Cache
    # -----------------------------

    query_cache[question] = answer

    print(answer)

############################################################
# Scenario 1
############################################################

print("=" * 60)
print("Scenario 1 : First Ask")
print("=" * 60)

ask_question(
    "Which API does our Task Management System use?"
)

############################################################
# Scenario 2
############################################################

print("\n")
print("=" * 60)
print("Scenario 2 : Cache Hit")
print("=" * 60)

ask_question(
    "Which API does our Task Management System use?"
)

############################################################
# Scenario 3
############################################################

print("\n")
print("=" * 60)
print("Scenario 3 : Grounding Test")
print("=" * 60)

ask_question(
    "What is the recipe for chocolate cake?"
)