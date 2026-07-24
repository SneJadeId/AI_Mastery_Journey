from typing import TypedDict
from langgraph.graph import StateGraph, END

##############################################################
# State
##############################################################

class DocumentState(TypedDict):

    srs: str

    requirements: list

    risks: list

    architecture: list

    test_cases: list

    final_report: str


##############################################################
# Document Analyzer
##############################################################

def document_analyzer(state: DocumentState):

    print("\n========== DOCUMENT ANALYZER ==========")

    print("Reading SRS Document...")

    return state


##############################################################
# Requirement Agent
##############################################################

def requirement_agent(state: DocumentState):

    print("\nRequirement Agent Running...")

    requirements = []

    for line in state["srs"].splitlines():

        line = line.strip()

        if line:
            requirements.append(line)

    state["requirements"] = requirements

    return state


##############################################################
# Risk Agent
##############################################################

def risk_agent(state: DocumentState):

    print("\nRisk Agent Running...")

    risks = []

    text = state["srs"].lower()

    if "payment" in text:
        risks.append("Payment security risk")

    if "encrypted" in text:
        risks.append("Encryption implementation required")

    if "1000 concurrent users" in text:
        risks.append("Performance and scalability risk")

    state["risks"] = risks

    return state


##############################################################
# Architecture Agent
##############################################################

def architecture_agent(state: DocumentState):

    print("\nArchitecture Agent Running...")

    architecture = [

        "Frontend",

        "Backend API",

        "Authentication Service",

        "Payment Gateway",

        "Database"

    ]

    state["architecture"] = architecture

    return state


##############################################################
# Test Case Agent
##############################################################

def test_case_agent(state: DocumentState):

    print("\nTest Case Agent Running...")

    tests = [

        "Verify User Registration",

        "Verify Login",

        "Verify Food Order",

        "Verify Payment",

        "Verify Menu Update",

        "Verify Admin Functions"

    ]

    state["test_cases"] = tests

    return state


##############################################################
# Merge Results
##############################################################

def merge_results(state: DocumentState):

    print("\nMerging Results...")

    report = f"""

================ FINAL REPORT ================

Requirements

{chr(10).join('- '+x for x in state["requirements"])}

----------------------------------------------

Risks

{chr(10).join('- '+x for x in state["risks"])}

----------------------------------------------

Suggested Architecture

{chr(10).join('- '+x for x in state["architecture"])}

----------------------------------------------

Suggested Test Cases

{chr(10).join('- '+x for x in state["test_cases"])}

"""

    state["final_report"] = report

    return state


##############################################################
# Human Review
##############################################################

def human_review(state: DocumentState):

    print("\n========== HUMAN REVIEW ==========")

    print("Review Status : Approved")

    return state


##############################################################
# Build Workflow
##############################################################

graph = StateGraph(DocumentState)

graph.add_node("Document Analyzer", document_analyzer)

graph.add_node("Requirement Agent", requirement_agent)

graph.add_node("Risk Agent", risk_agent)

graph.add_node("Architecture Agent", architecture_agent)

graph.add_node("Test Case Agent", test_case_agent)

graph.add_node("Merge Results", merge_results)

graph.add_node("Human Review", human_review)

graph.set_entry_point("Document Analyzer")

graph.add_edge("Document Analyzer", "Requirement Agent")

graph.add_edge("Requirement Agent", "Risk Agent")

graph.add_edge("Risk Agent", "Architecture Agent")

graph.add_edge("Architecture Agent", "Test Case Agent")

graph.add_edge("Test Case Agent", "Merge Results")

graph.add_edge("Merge Results", "Human Review")

graph.add_edge("Human Review", END)

workflow = graph.compile()

##############################################################
# Main
##############################################################

if __name__ == "__main__":

    with open("sample_srs.txt", "r", encoding="utf-8") as f:
        srs = f.read()

    result = workflow.invoke(
        {
            "srs": srs
        }
    )

    print(result["final_report"])