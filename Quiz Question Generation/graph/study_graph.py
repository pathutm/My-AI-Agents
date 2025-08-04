from langgraph.graph import StateGraph
from agents.summarizer_agent import summarizer_agent
from agents.quiz_agent import quiz_agent

class StudyGraphState(dict):
    """Holds input and outputs for the LangGraph."""
    input_text: str
    summary: str = ""
    quiz: str = ""

def build_study_graph():
    graph = StateGraph(StudyGraphState)

    # Summarizer node
    graph.add_node("summarize", lambda state: {
        "summary": summarizer_agent.invoke(state["input_text"])
    })

    # Quiz node
    graph.add_node("quiz", lambda state: {
        "quiz": quiz_agent.invoke(state["input_text"])
    })

    # Define execution flow
    graph.set_entry_point("summarize")
    graph.add_edge("summarize", "quiz")

    return graph.compile()
