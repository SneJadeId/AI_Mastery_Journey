from langchain_community.document_loaders import TextLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import FakeEmbeddings

loader = TextLoader("game_rules.txt")

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(

chunk_size=100,

chunk_overlap=20

)

docs = splitter.split_documents(documents)

db = FAISS.from_documents(

docs,

FakeEmbeddings(size=768)

)

retriever = db.as_retriever()

results = retriever.invoke(

"How many points is the golden token worth?"

)

print(results[0].page_content)