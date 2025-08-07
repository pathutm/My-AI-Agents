import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def get_gemini_llm():
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.3,
        google_api_key=api_key  # Use API key explicitly
    )
