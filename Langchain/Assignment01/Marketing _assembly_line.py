from company_llm import CompanyLLM

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser

llm = CompanyLLM()

prompt1 = PromptTemplate(

input_variables=["product_name"],

template="""
Generate a catchy FIVE WORD English slogan.

Product

{product_name}
"""

)

prompt2 = PromptTemplate(

input_variables=["slogan"],

template="""
Translate into French.

{slogan}
"""

)

chain = (

prompt1

| llm

| StrOutputParser()

| {

"slogan": lambda x:x

}

| prompt2

| llm

| StrOutputParser()

)

print(

chain.invoke({

"product_name":"Wireless Earbuds"

})

)