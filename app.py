import os
import streamlit as st
from qa_chain import load_vectorstore, create_qa_chain

def main():
    st.title("Ilarischmidt.com AI Botti")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    # Load the QA chain only once per session
    if "qa_chain" not in st.session_state:
        vectorstore = load_vectorstore("faiss_store", openai_api_key)
        st.session_state.qa_chain = create_qa_chain(vectorstore, openai_api_key)
    
    user_question = st.text_input("Hei! Olen Ilarin tekemä langchain pohjainen ai botti. Ilari on kerännyt bloginsa tietopankkiini ja vastailen kysymyksiin tähän tietoon perustuen! Kielimallina toimii GPT3. Kysy minulta mitä tahansa blogiin liittyen:")
    
    if st.button("Lähetä") and user_question.strip():
        result = st.session_state.qa_chain(user_question)
        st.write("**Vastaus:**", result["result"])
        
        with st.expander("Sources"):
            for doc in result["source_documents"]:
                file_path = doc.metadata.get("source", "")
                # Extract the file name
                file_name = os.path.basename(file_path)
                # Remove the file extension
                title = os.path.splitext(file_name)[0]
                # Optionally, replace underscores with spaces
                title = title.replace("_", " ")
                st.write(f"- {title}")

if __name__ == "__main__":
    main()
