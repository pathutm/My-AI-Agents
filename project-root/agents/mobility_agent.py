from langchain.agents import initialize_agent, AgentType
from tools.mobility_tool import evaluate_mobility
from utils.llm_config import get_gemini_llm
import json

def run_mobility_readiness_agent(user_inputs: dict) -> str:
    llm = get_gemini_llm()
    
    agent = initialize_agent(
        tools=[evaluate_mobility],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    # ✅ Pass raw JSON string as input to the agent
    return agent.invoke({"input": json.dumps(user_inputs, separators=(",", ":"))
    })

