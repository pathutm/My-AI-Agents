from langchain.agents import initialize_agent, AgentType
from tools.progression_tools import career_progression_tool
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def get_career_progression_agent():
    tools = [career_progression_tool]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    return agent

def run_career_progression_mapper(specialty_data_str: str) -> str:
    agent = get_career_progression_agent()
    return agent.run(specialty_data_str)
