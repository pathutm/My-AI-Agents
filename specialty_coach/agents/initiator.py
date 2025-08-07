from langchain.agents import initialize_agent, AgentType
from langchain.agents.agent_executor import AgentExecutor
from langchain.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI

from agents.specialty_strength_agent import specialty_strength_tool
from agents.career_progression_mapper_agent import career_progression_tool

def extract_observation_json(text: str) -> str:
    """Extract JSON from a string line starting with 'Observation:'"""
    for line in text.splitlines():
        if "Observation:" in line:
            return line.replace("Observation:", "").strip()
    raise ValueError("No JSON found in specialty_strength_tool output.")

def run_all_agents(clinical_text: str, career_goals: str):
    print("🚀 Running Specialty Strength Analyzer Agent...")

    # Agent 1: Specialty Analyzer
    tools_1 = [Tool.from_function(specialty_strength_tool)]
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
    agent_1 = initialize_agent(tools_1, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    output_1 = agent_1.run(clinical_text)
    print("🔍 Raw output from specialty_strength_agent:\n", output_1)

    parsed_specialty = extract_observation_json(output_1)

    print("✅ Specialty JSON extracted:", parsed_specialty)

    # Agent 2: Career Mapper
    print("🚀 Running Career Progression Mapper Agent...")

    tools_2 = [Tool.from_function(career_progression_tool)]
    agent_2 = initialize_agent(tools_2, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    output_2 = agent_2.run(parsed_specialty)
    print("🎯 Raw output from career_progression_agent:\n", output_2)

    return {
        "specialty_analysis": parsed_specialty,
        "career_paths": output_2
    }
