from langchain_google_genai import ChatGoogleGenerativeAI
from agents.specialty_strength_analyzer import get_specialty_strength_agent
from agents.career_progression_mapper import get_career_progression_agent
import json
import os
from dotenv import load_dotenv

load_dotenv()

def run_all_agents(clinical_text: str, career_goals: str):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

    # 1. Run Specialty Strength Agent
    specialty_agent = get_specialty_strength_agent(llm)
    specialty_result = specialty_agent.run(clinical_text)

    # Parse output
    parsed_specialty = json.loads(specialty_result)

    # 2. Run Career Progression Agent
    progression_agent = get_career_progression_agent(llm)
    progression_result = progression_agent.run(
        f"Specialty Data: {json.dumps(parsed_specialty)}\nCareer Goals: {career_goals}"
    )

    return {
        "specialty_analysis": parsed_specialty,
        "career_progression": progression_result
    }
