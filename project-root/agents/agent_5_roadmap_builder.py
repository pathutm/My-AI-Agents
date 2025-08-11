from langchain.agents import initialize_agent, AgentType
from tools.roadmap_tool import build_career_roadmap
from utils.llm_config import get_gemini_llm
import json

def run_roadmap_builder_agent(agent_inputs: dict) -> str:
    """
    Runs the Roadmap Builder Agent.
    Expects agent_inputs to be a dict containing:
      specialty_analysis, career_paths, certifications, mobility_result
    """
    llm = get_gemini_llm()

    agent = initialize_agent(
        tools=[build_career_roadmap],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    # Directly pass the dict instead of building a big natural language prompt
    # ZERO_SHOT_REACT_DESCRIPTION will handle calling the tool
    payload = {"input": json.dumps(agent_inputs, ensure_ascii=False)}

    result = agent.invoke(payload)
    return result.get("output", str(result))
