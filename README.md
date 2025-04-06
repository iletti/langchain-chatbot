# LangChain Blog Q&A Chatbot

This project demonstrates how to build a Q&A chatbot using LangChain and OpenAI that extracts and ingests your blog posts, builds a FAISS vector store for document retrieval, and answers user queries by retrieving relevant content from your blog. The app is built with Streamlit and can be deployed on Streamlit Cloud, with the option to embed it as an iframe on your website.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Workflow](#workflow)
  - [1. Extracting Blog Posts](#1-extracting-blog-posts)
  - [2. Data Ingestion & Chunking](#2-data-ingestion--chunking)
  - [3. Building the Vector Store](#3-building-the-vector-store)
  - [4. QA Chain Setup](#4-qa-chain-setup)
  - [5. Running the App Locally](#5-running-the-app-locally)
- [Deployment on Streamlit Cloud](#deployment-on-streamlit-cloud)
- [Embedding as an iFrame](#embedding-as-an-iframe)
- [Troubleshooting & Notes](#troubleshooting--notes)
- [License](#license)

## Project Overview

This project creates an interactive chatbot that uses LangChain to answer questions based on your blog content. The workflow includes:

1. **Extracting Blog Posts:** Parsing a Ghost JSON export into individual text files.
2. **Data Ingestion:** Loading and chunking blog posts into manageable pieces for the language model.
3. **Vector Store Creation:** Generating embeddings for each chunk and storing them in a FAISS vector store.
4. **QA Chain Setup:** Building a retrieval-based QA chain that uses the vector store to find relevant blog sections and passes them to an LLM (ChatGPT) to generate answers.
5. **Streamlit App:** Creating a user-friendly web interface to interact with the chatbot.
6. **Deployment & Embedding:** Deploying the app on Streamlit Cloud and embedding it as an iframe on your site.

## Features

- Converts blog posts into text chunks for LLM processing.
- Uses OpenAI embeddings and FAISS for efficient document retrieval.
- Provides a Q&A interface powered by ChatGPT.
- Deployable on Streamlit Cloud.
- Option to embed the chatbot in your website via an iframe (e.g., an expanding chat bubble).

## Requirements

- Python 3.9 or higher
- [Streamlit](https://streamlit.io)
- [langchain-community](https://pypi.org/project/langchain-community/)
- [langchain-openai](https://pypi.org/project/langchain-openai/)
- [faiss-cpu](https://github.com/facebookresearch/faiss) (or appropriate FAISS package)
- Git (for version control and deployment)
- A valid OpenAI API key

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/langchain-chatbot.git
   cd langchain-chatbot
Create and Activate a Virtual Environment:

bash
Copy
python -m venv blog_qa
# On Windows:
.\blog_qa\Scripts\Activate.ps1
# On macOS/Linux:
source blog_qa/bin/activate
Install Dependencies:

bash
Copy
pip install -U streamlit langchain-community langchain-openai faiss-cpu
Generate requirements.txt:

bash
Copy
pip freeze > requirements.txt
Workflow
1. Extracting Blog Posts
Use the provided extract_posts.py script to convert your Ghost JSON export file into individual text files in a folder (e.g., blog_posts).

2. Data Ingestion & Chunking
The ingest.py script reads all .txt (and optionally .md) files from the blog_posts folder, handles encoding issues, and splits each file into smaller chunks (e.g., 1000 characters per chunk with overlap) using LangChain’s RecursiveCharacterTextSplitter.

Run:

bash
Copy
python ingest.py
3. Building the Vector Store
The build_vectorstore.py script loads the chunked documents, generates embeddings using OpenAIEmbeddings, and stores them in a FAISS vector store. It then saves the index locally to avoid rebuilding it each time.

Run:

bash
Copy
python build_vectorstore.py
4. QA Chain Setup
The qa_chain.py script loads the FAISS vector store (using the flag allow_dangerous_deserialization=True for pickle file loading), sets up a retrieval-based QA chain with ChatOpenAI, and tests the chain with an example query.

Run:

bash
Copy
python qa_chain.py
5. Running the App Locally
The main Streamlit app (app.py) provides an interactive interface where users can ask questions. The app displays the answer along with the titles of the source blog posts.

Run:

bash
Copy
streamlit run app.py
Deployment on Streamlit Cloud
Push Your Code to GitHub:

Follow standard Git commands to commit and push your project to a public GitHub repository.

Deploy on Streamlit Cloud:

Go to Streamlit Cloud and sign in with GitHub.

Click on New app, select your repository, branch (e.g., main), and specify the app file path (app.py).

In the app settings, add your OpenAI API key as a secret:

ini
Copy
OPENAI_API_KEY="sk-yourapikeyhere"
Click Deploy and wait for the app to launch.

Embedding as an iFrame
To embed your Streamlit app as an iframe on your website (for instance, as an expanding chat interface):

Get the Streamlit App URL:
Once deployed, your app will have a public URL (e.g., https://your-app-name.streamlit.app).

Embed in Your Site:

Insert the following HTML snippet where you want the chatbot to appear on your website:

html
Copy
<iframe src="https://your-app-name.streamlit.app" width="350" height="500" style="border:none; overflow:hidden;" scrolling="no" allowtransparency="true" allowfullscreen="true"></iframe>
Customize the width, height, and styling as needed. You can add JavaScript to make it expandable or create a chat bubble interface if desired.

Troubleshooting & Notes
Deprecation Warnings:
The project currently shows deprecation warnings for some LangChain components. Update the import paths as follows to future-proof your code:

Use from langchain_openai import OpenAIEmbeddings

Use from langchain_community.vectorstores import FAISS

Use from langchain_community.chat_models import ChatOpenAI

Security Notice:
The FAISS vector store is loaded with allow_dangerous_deserialization=True. Only use this flag if you trust the source of the pickle file (i.e., your own generated file).

Environment Variables:
Make sure to set your OpenAI API key in your environment or through Streamlit Cloud's secrets.
