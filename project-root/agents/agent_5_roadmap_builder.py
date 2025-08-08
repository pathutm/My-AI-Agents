from langchain.agents import initialize_agent, AgentType
from tools.roadmap_tool import build_career_roadmap
from utils.llm_config import get_gemini_llm
import json

def run_roadmap_builder_agent(agent_inputs: dict) -> str:
    llm = get_gemini_llm()

    agent = initialize_agent(
        tools=[build_career_roadmap],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent.invoke({
        "input": json.dumps(agent_inputs)
    })
