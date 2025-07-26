# Libraries and Modules
import os
from langchain.chains import RetrievalQA
# from langchain.llms import OpenAI
from langchain_openai import OpenAI
# from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
# from langchain.document_loaders import UnstructuredFileLoader
from langchain_community.document_loaders import TextLoader
# from langchain.text_splitter import CharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter
# from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma


# OpenAI key
os.environ['OPENAI_API_KEY'] = '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'


# OpenAI LLM 
llm = OpenAI(temperature=0.9, verbose=True)



#Document Loader and Splitter
loader = TextLoader("webpages_text.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Embeddings and vectorstores
embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_documents(texts, embeddings)

#Chain 
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

# Prompt
query = "What is CIMA?"
# response = qa.run(query)
response = qa.invoke(query)
# print(response)
print(response['result'])