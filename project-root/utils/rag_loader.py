from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

import os

def load_certification_vectorstore(verbose: bool = False):
    file_path = "rag_store/certifications.txt"
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Missing file: {file_path}")

    loader = TextLoader(file_path)
    docs = loader.load()

    if verbose:
        print(f"✅ Loaded {len(docs)} documents from {file_path}")

    text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    chunks = text_splitter.split_documents(docs)

    if verbose:
        print(f"📄 Split into {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    if verbose:
        print("✅ FAISS index built")

    return vectorstore.as_retriever()
