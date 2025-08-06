from tools.specialty_tools import specialty_strength_tool
from langchain.agents import initialize_agent, AgentType
from langchain_core.language_models import BaseLanguageModel

def get_specialty_strength_agent(llm: BaseLanguageModel):
    return initialize_agent(
        tools=[specialty_strength_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
