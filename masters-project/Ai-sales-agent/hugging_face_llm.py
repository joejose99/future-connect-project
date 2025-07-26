from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import HuggingFacePipeline
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_core.runnables import Runnable
from transformers import pipeline

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress INFO and WARNING logs from TensorFlow

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning

warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)

import warnings
warnings.filterwarnings("ignore")

from langchain_huggingface import HuggingFacePipeline


import shutil
shutil.rmtree("db", ignore_errors=True)  # Wipe old DB


 

# Load documents
loader = TextLoader('webpages_strath.txt')
documents = loader.load()
 
# Split documents
text_splitter = CharacterTextSplitter(chunk_size=255, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Embedding and vector store
#embedding_model = HuggingFaceEmbeddings()
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")  # 768-dim

#vectordb = Chroma.from_documents(texts, embedding_model, persist_directory="db")

vectordb = Chroma.from_documents(
    texts,
    embedding_model,
    persist_directory="db"
)
vectordb.persist()


vectordb.persist()

# HuggingFace Pipeline LLM setup
hf_pipeline = pipeline("text2text-generation", model="google/flan-t5-base", max_length=512)
llm = HuggingFacePipeline(pipeline=hf_pipeline)

# RetrievalQA chain
retriever = vectordb.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

# Ask a question
#query = "What is the cost of your data science course?"
query = "What are the entry requirement for masters in data science course?"
#query = "What is Mathematics & Statistics"
response = qa_chain.invoke({"query": query})
print("\n query: ",query)
print(" ")
print("Response: ",response["result"])
