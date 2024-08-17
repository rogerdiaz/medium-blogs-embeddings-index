import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
load_dotenv()

if __name__ == '__main__':
    print("Ingesting...")
    loader = TextLoader("/Users/rogerartemiodiazfuentes/Desktop/Diseno_e_innovacion_con_AI/intro-to-vector-dbs/mediumblog1.txt")
    document = loader.load()
    print("Splitting...")
