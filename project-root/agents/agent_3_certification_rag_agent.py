from langchain.agents import initialize_agent, AgentType
from tools.certification_suggester_tool import suggest_certifications
from utils.llm_config import get_gemini_llm

def create_certification_agent():
    llm = get_gemini_llm()
    agent = initialize_agent(
        tools=[suggest_certifications],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent

def run_certification_suggester(progression_summary: str) -> str:
    agent = create_certification_agent()
    return agent.run(progression_summary)
