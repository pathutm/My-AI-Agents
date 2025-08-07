from langchain.tools import tool
from utils.rag_loader import load_certification_vectorstore
from langchain.chains import RetrievalQA
from utils.llm_config import get_gemini_llm

@tool
def suggest_certifications(input: str) -> str:
    """
    Suggest required certifications or fellowships based on given career progression path.
    """
    retriever = load_certification_vectorstore()
    llm = get_gemini_llm()

    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )

    return rag_chain.run(input)
