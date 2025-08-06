# agents/career_progression_mapper.py

from tools.progression_tools import career_progression_tool
from langchain.agents import initialize_agent, AgentType
from langchain_core.language_models import BaseLanguageModel

def get_career_progression_agent(llm: BaseLanguageModel):
    tools = [career_progression_tool]
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
