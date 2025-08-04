from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from config.env_loader import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEMINI_API_KEY)

@tool
def summarize_text(input_text: str) -> str:
    """Summarizes the given text into a concise summary."""
    prompt = f"Summarize the following course material:\n\n{input_text}"
    return llm.invoke(prompt)
