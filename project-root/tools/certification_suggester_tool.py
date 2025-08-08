# tools/certification_suggester_tool.py

from utils.rag_loader import load_certification_vectorstore
from langchain.chains import RetrievalQA
from utils.llm_config import get_gemini_llm

def suggest_certifications_rag(input_text: str) -> str:
    """
    Use RAG to suggest certifications or fellowships based on given career progression.
    """
    retriever = load_certification_vectorstore()
    llm = get_gemini_llm()

    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )

    return rag_chain.run(input_text)
