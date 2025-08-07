import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.career_mapper_prompt import CAREER_PROGRESSION_PROMPT

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

@tool
def career_progression_tool(specialty_data: str) -> str:
    """
    Given the specialty and strengths data, suggest 3+ logical career progression paths.
    Input should be a string containing both specialty and career goal info.
    """
    career_goals = "I am looking to grow in a specialized respiratory care or critical care role."

    prompt = CAREER_PROGRESSION_PROMPT.format(
        input_text=specialty_data,
        career_goals=career_goals
    )

    raw_output = llm.invoke(prompt).content

    # Just return the full output — it's useful and avoids breaking downstream
    return raw_output
