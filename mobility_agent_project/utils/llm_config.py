import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # Loads .env variables

def get_gemini_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # ✅ Use the faster Gemini model
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.2
    )

