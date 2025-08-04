from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from config.env_loader import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEMINI_API_KEY)

@tool
def generate_quiz(input_text: str) -> str:
    """Generates 5 multiple-choice questions (MCQs) based on the given text."""
    prompt = (
        f"Create 5 multiple-choice quiz questions based on the following course material. "
        f"Each question should have 4 options labeled A-D, with the correct answer indicated in parentheses at the end.\n\n{input_text}"
    )
    return llm.invoke(prompt)
