import os
from langchain_openai import OpenAIEmbeddings  # Updated import per deprecation warning
from langchain_community.vectorstores import FAISS  # Updated import per deprecation warning
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI  # Updated import per deprecation warning

def load_vectorstore(faiss_path: str, openai_api_key: str):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.load_local(faiss_path, embeddings, allow_dangerous_deserialization=True)
    return vectorstore

def create_qa_chain(vectorstore, openai_api_key: str):
    llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

if __name__ == "__main__":
    faiss_path = "faiss_store"
    openai_api_key = os.getenv("OPENAI_API_KEY")
    vectorstore = load_vectorstore(faiss_path, openai_api_key)
    qa_chain = create_qa_chain(vectorstore, openai_api_key)
    
    # Test the chain with an example query
    query = "mitä mieltä Ilari on chat gpt:stä?"
    result = qa_chain(query)
    print("Answer:", result['result'])
    print("Sources:", result['source_documents'])
