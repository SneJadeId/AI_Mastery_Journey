from langchain_core.documents import Document



from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

# Keep this if there is no standalone FAISS package installed
from langchain_community.vectorstores import FAISS

from company_llm import CompanyLLM


#####################################################
# Load Documents
#####################################################

loader1 = TextLoader("policy_2022.txt")

loader2 = TextLoader("policy_2024.txt")

docs_2022 = loader1.load()

docs_2024 = loader2.load()

#####################################################
# Metadata
#####################################################

for doc in docs_2022:
    doc.metadata["year"] = 2022

for doc in docs_2024:
    doc.metadata["year"] = 2024

documents = docs_2022 + docs_2024

#####################################################
# Split
#####################################################

splitter = RecursiveCharacterTextSplitter(

    chunk_size=200,

    chunk_overlap=50

)

chunks = splitter.split_documents(documents)

#####################################################
# Embeddings
#####################################################

embedding = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)

#####################################################
# FAISS
#####################################################

db = FAISS.from_documents(

    chunks,

    embedding

)

#####################################################
# Custom Retrieval
#####################################################

def retrieve(query, year):

    docs = db.similarity_search(

        query,

        k=5

    )

    filtered = [

        d

        for d in docs

        if d.metadata["year"] == year

    ]

    return filtered


#####################################################
# LLM
#####################################################

llm = CompanyLLM()

#####################################################
# Main
#####################################################

query = "What is the WFH policy?"

filter_year = 2024

retrieved = retrieve(

    query,

    filter_year

)

context = "\n".join(

    d.page_content

    for d in retrieved

)

prompt = f"""

Answer ONLY using the following context.

If the answer is not available say

"I do not have enough information."

Context

{context}

Question

{query}

"""

answer = llm.invoke(prompt)

#####################################################
# Output
#####################################################

print("="*60)

print("User Query")

print(query)

print()

print("Active Filter")

print(filter_year)

print()

print("Retrieved Context")

print(context)

print()

print("LLM Final Answer")

print(answer)

print("="*60)