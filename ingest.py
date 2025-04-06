import os
import glob
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

def load_and_chunk_blog_posts(blog_folder_path: str, chunk_size=1000, chunk_overlap=100):
    """Load text from blog posts (using proper error handling) and split into smaller chunks."""
    all_docs = []
    
    # Find all .txt and .md files in the folder
    file_paths = glob.glob(os.path.join(blog_folder_path, '*.txt')) + \
                 glob.glob(os.path.join(blog_folder_path, '*.md'))
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    
    for path in file_paths:
        try:
            # Open the file with UTF-8 encoding and replace any undecodable characters
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except Exception as e:
            print(f"Failed to load {path}: {e}")
            continue
        
        # Create a Document manually from the file content
        doc = Document(page_content=content, metadata={"source": path})
        # Split the document into smaller chunks
        chunks = text_splitter.split_text(doc.page_content)
        for chunk in chunks:
            all_docs.append(Document(page_content=chunk, metadata={"source": path}))
    
    return all_docs

if __name__ == "__main__":
    docs = load_and_chunk_blog_posts("blog_posts")
    print(f"Loaded and split into {len(docs)} chunks")
