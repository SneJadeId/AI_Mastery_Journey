from company_llm import CompanyLLM

from langchain_core.callbacks import BaseCallbackHandler

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser

class MyLogger(BaseCallbackHandler):

    def on_llm_start(self,*args,**kwargs):

        print("LLM Started")

    def on_llm_end(self,*args,**kwargs):

        print("LLM Finished")

llm = CompanyLLM()

llm.callbacks=[MyLogger()]

prompt = PromptTemplate(

input_variables=["review"],

template="""

Review

{review}

Return sentiment only.

"""

)

chain = prompt | llm | StrOutputParser()

result = chain.invoke({

"review":"Very bad product."

})

print(result)

print()

print("========== RECEIPT ==========")

print("Prompt Tokens      : N/A")

print("Completion Tokens  : N/A")

print("Total Tokens       : N/A")

print("Total Cost         : N/A")

print("=============================")