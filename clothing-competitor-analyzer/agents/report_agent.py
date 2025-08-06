from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.templates import REPORT_PROMPT

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.4)

def generate_competitor_report(data: dict) -> str:
    prompt = REPORT_PROMPT.format(search_results=data["search_results"])
    response = llm.invoke(prompt)
    return response.content
