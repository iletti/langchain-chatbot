import os
from langchain_openai import OpenAIEmbeddings  # Updated import
from langchain_community.vectorstores import FAISS  # Updated import
from ingest import load_and_chunk_blog_posts

def build_faiss_vectorstore(docs, openai_api_key: str):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

if __name__ == "__main__":
    docs = load_and_chunk_blog_posts("blog_posts")
    openai_api_key = os.getenv("OPENAI_API_KEY")  # Make sure this is set!
    vectorstore = build_faiss_vectorstore(docs, openai_api_key)
    
    # Save the vector store to disk to avoid rebuilding every time
    faiss_path = "faiss_store"
    vectorstore.save_local(faiss_path)
    print("FAISS vector store built and saved locally!")
