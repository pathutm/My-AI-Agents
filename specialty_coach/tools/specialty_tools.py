from langchain.agents import initialize_agent, AgentType
from langchain.agents.agent import AgentExecutor
from tools.specialty_strength_tool import specialty_strength_tool

def get_specialty_strength_agent(llm) -> AgentExecutor:
    tools = [specialty_strength_tool]

    agent_executor = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # or OPENAI_FUNCTIONS if using OpenAI
        verbose=True
    )
    return agent_executor
