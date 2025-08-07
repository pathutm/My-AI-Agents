from langchain.agents import initialize_agent, AgentType
from tools.progression_mapper_tool import map_career_progression
from utils.llm_config import get_gemini_llm

def create_progression_mapper_agent():
    llm = get_gemini_llm()

    agent = initialize_agent(
        tools=[map_career_progression],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True  # Handles output format issues
    )
    return agent

def run_career_progression(input_text: str) -> str:
    agent = create_progression_mapper_agent()
    return agent.run(input_text)
