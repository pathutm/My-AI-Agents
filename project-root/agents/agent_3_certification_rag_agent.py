from langchain.chains import RetrievalQA
from utils.llm_config import get_gemini_llm
from utils.rag_loader import load_certification_vectorstore

def run_certification_suggester(agent1_output: str) -> str:
    """
    Uses RAG to suggest certifications based on the specialties found in Agent 1's output.    """
    retriever = load_certification_vectorstore(verbose=True)
    llm = get_gemini_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )

    # Ask directly using the specialties
    query = f"What certifications are relevant for specialties mentioned in this text: {agent1_output}"
    return qa_chain.run(query)
