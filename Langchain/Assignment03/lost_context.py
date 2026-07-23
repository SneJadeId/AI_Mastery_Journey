from langchain_core.documents import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import HuggingFaceEmbeddings

from company_llm import ask_llm

############################################################

tricky_document = """
Section 1: The company Jade Global is launching a massive new
internal initiative called Project Phoenix. This project will
restructure the entire cloud infrastructure.

Section 2: Employees must adhere to the standard office hours of
9:00 AM to 5:00 PM. Remote work is permitted on Tuesdays and
Thursdays.

Section 3: The cafeteria will now offer extended hours.

Section 4: All IT support tickets must be filed through Jira.

Section 5: Holiday party is December 15th.

Section 6: Parking rules updated.

Section 7: Health insurance begins in October.

Section 8: Cybersecurity training is mandatory.

Section 9: Regarding the cloud restructure initiative mentioned
earlier, the final deadline is December 31st, 2026.
The approved budget is $500,000.
"""

############################################################

document = Document(page_content=tricky_document)

############################################################

splitter = RecursiveCharacterTextSplitter(

    chunk_size=350,

    chunk_overlap=120

)

docs = splitter.split_documents([document])

############################################################

embedding = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)

############################################################

db = FAISS.from_documents(

    docs,

    embedding

)

############################################################

query = "What is the deadline and budget for Project Phoenix?"

results = db.similarity_search(

    query,

    k=2

)

############################################################

context = ""

for doc in results:

    context += doc.page_content + "\n\n"

############################################################

prompt = f"""
Answer ONLY from the context.

Context

{context}

Question

{query}

If answer not present,
reply

I do not know.
"""

############################################################

answer = ask_llm(prompt)

############################################################

print("=" * 60)
print("QUERY")
print("=" * 60)

print(query)

print("\n")

print("=" * 60)
print("RETRIEVED CONTEXT")
print("=" * 60)

print(context)

print("\n")

print("=" * 60)
print("LLM ANSWER")
print("=" * 60)

print(answer)

'''
Chunk Size = 350

Chunk Overlap = 120

Initially, I used a chunk overlap of 0. This caused the vector
database to retrieve only Section 9, where the document referred
to "the cloud restructure initiative" without mentioning the
name "Project Phoenix."

As a result, the LLM could not confidently connect the initiative
to Project Phoenix.

Increasing the overlap to 120 characters ensured that the ending
of Section 1 overlapped with the beginning of the following chunk,
preserving the semantic relationship between Project Phoenix and
its deadline and budget.

This improved retrieval quality and eliminated context fragmentation.
'''