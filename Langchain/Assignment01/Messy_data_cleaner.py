from company_llm import CompanyLLM

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser

llm = CompanyLLM()

prompt = PromptTemplate(

input_variables=["messy_review"],

template="""
Read the review.

Return ONLY

Sentiment: Positive/Negative,
Core Issue: Brief Summary

Review

{messy_review}
"""

)

chain = prompt | llm | StrOutputParser()

print(

chain.invoke({

"messy_review":

"""I bought this blender yesterday and it's absolutely terrible!
The lid flew off while making a smoothie.
I want a refund."""

})

)