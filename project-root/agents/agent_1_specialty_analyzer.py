from langchain.agents import initialize_agent, AgentType
from langchain.prompts import PromptTemplate
from tools.specialty_parser_tool import parse_specialty_experience
from utils.llm_config import get_gemini_llm

def load_prompt():
    with open("prompts/specialty_parser_prompt.txt", "r") as f:
        return f.read()

def create_specialty_analyzer_agent():
    llm = get_gemini_llm()

    tools = [parse_specialty_experience]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True  # ✅ This enables terminal logging
    )

    return agent
