"""
Assignment 1

Self Correcting LangChain Agent

Author : Sneha Sharma
"""

from company_llm import CompanyLLM

import wikipedia

llm = CompanyLLM()


####################################################
# SEARCH TOOL
####################################################

def search_tool(query):

    try:

        page = wikipedia.page(query)

        summary = wikipedia.summary(query, sentences=1)

        year = ""

        for word in summary.split():

            if word.isdigit() and len(word) == 4:

                year = word
                break

        return year

    except Exception:

        return "Not Found"


####################################################
# CALCULATOR TOOL
####################################################

def calculator_tool(expression):

    return eval(expression)


####################################################
# AGENT
####################################################

def self_correcting_agent(user_query):

    print("\n" + "=" * 70)
    print("SELF CORRECTING LANGCHAIN AGENT")
    print("=" * 70)

    print("\nUser Query:")
    print(user_query)

    ################################################

    thought1 = llm.invoke(

f"""
A user asked:

{user_query}

You need multiplication.

Before solving, think whether you already know every value.

Reply in one short paragraph.
"""

    )

    print("\nThought 1:")
    print(thought1)

    ################################################

    print("\nAction 1:")
    print("Search Tool")

    birth_year = search_tool("Albert Einstein")

    print("\nObservation 1:")
    print("Albert Einstein Birth Year =", birth_year)

    ################################################

    thought2 = llm.invoke(

f"""
Now we know

Albert Einstein Birth Year = {birth_year}

Explain why the calculator should be used next.
"""

    )

    print("\nThought 2:")
    print(thought2)

    ################################################

    print("\nAction 2:")
    print(f"Calculator Tool : {birth_year} * 5")

    answer = calculator_tool(f"{birth_year}*5")

    ################################################

    print("\nFinal Answer:")
    print(answer)

    ################################################

    explanation = llm.invoke(

f"""
Question

{user_query}

Birth year

{birth_year}

Result

{answer}

Explain in 2 lines how the answer was obtained.
"""

    )

    print("\nLLM Explanation:")
    print(explanation)

    print("\n" + "=" * 70)


####################################################

if __name__ == "__main__":

    query = "Multiply the birth year of Albert Einstein by 5."

    self_correcting_agent(query)