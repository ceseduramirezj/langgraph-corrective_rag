from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Puede ser un proceso ETL

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

urls = [
    "https://github.com/lilianweng/lilianweng.github.io/tree/master/posts/2023-06-23-agent",
    "https://github.com/lilianweng/lilianweng.github.io/tree/master/posts/2023-03-15-prompt-engineering",
    "https://github.com/lilianweng/lilianweng.github.io/tree/master/posts/2023-10-25-adv-attack-llm",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250, chunk_overlap=0
)
doc_splits = text_splitter.split_documents(docs_list)

#vectorstore = Chroma.from_documents(
#    documents= doc_splits,
#    collection_name= "rag-chroma",
#    embedding= embeddings,
#    persist_directory="./.chroma"
#)

retriever = Chroma(
    collection_name= "rag-chroma",
    persist_directory= "./.chroma",
    embedding_function= embeddings,
).as_retriever()