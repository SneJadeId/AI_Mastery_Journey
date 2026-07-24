from typing import TypedDict
from langgraph.graph import StateGraph, END

##########################################################
# State Definition
##########################################################

class ExpenseState(TypedDict):
    expense_usd: float
    taxed_amount: float
    amount_inr: float
    decision: str


##########################################################
# Node 1
# Add 10% Tax
##########################################################

def add_tax(state: ExpenseState):

    expense = state["expense_usd"]

    taxed = expense * 1.10

    print("\nStep 1 : Tax Added")
    print(f"Original Expense : ${expense:.2f}")
    print(f"After 10% Tax    : ${taxed:.2f}")

    state["taxed_amount"] = taxed

    return state


##########################################################
# Node 2
# Convert to INR
##########################################################

USD_TO_INR = 87.0


def convert_currency(state: ExpenseState):

    inr = state["taxed_amount"] * USD_TO_INR

    state["amount_inr"] = inr

    print("\nStep 2 : Currency Conversion")
    print(f"Amount in INR : ₹{inr:.2f}")

    return state


##########################################################
# Router
##########################################################

def approval_router(state: ExpenseState):

    expense = state["expense_usd"]

    if expense <= 100:
        return "auto"

    elif expense <= 1000:
        return "manager"

    else:
        return "finance"


##########################################################
# Node 3
##########################################################

def auto_approval(state: ExpenseState):

    state["decision"] = "Auto Approved"

    print("\nStep 3 : Auto Approval")

    return state


##########################################################
# Node 4
##########################################################

def manager_approval(state: ExpenseState):

    state["decision"] = "Manager Approval Required"

    print("\nStep 3 : Manager Approval")

    return state


##########################################################
# Node 5
##########################################################

def finance_approval(state: ExpenseState):

    state["decision"] = "Finance Department Approval Required"

    print("\nStep 3 : Finance Approval")

    return state


##########################################################
# Build Graph
##########################################################

graph = StateGraph(ExpenseState)

graph.add_node("tax", add_tax)

graph.add_node("convert", convert_currency)

graph.add_node("auto", auto_approval)

graph.add_node("manager", manager_approval)

graph.add_node("finance", finance_approval)

graph.set_entry_point("tax")

graph.add_edge("tax", "convert")

graph.add_conditional_edges(
    "convert",
    approval_router,
    {
        "auto": "auto",
        "manager": "manager",
        "finance": "finance"
    }
)

graph.add_edge("auto", END)

graph.add_edge("manager", END)

graph.add_edge("finance", END)

workflow = graph.compile()

##########################################################
# Main
##########################################################

if __name__ == "__main__":

    print("=" * 60)
    print("SMART EXPENSE PROCESSING SYSTEM")
    print("=" * 60)

    expense = float(input("\nEnter Expense Amount (USD): "))

    result = workflow.invoke(
        {
            "expense_usd": expense
        }
    )

    print("\n" + "=" * 60)
    print("FINAL RESULT")
    print("=" * 60)

    print(f"Original Expense : ${result['expense_usd']:.2f}")
    print(f"Taxed Amount     : ${result['taxed_amount']:.2f}")
    print(f"Converted Amount : ₹{result['amount_inr']:.2f}")
    print(f"Decision         : {result['decision']}")