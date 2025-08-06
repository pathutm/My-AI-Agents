from langgraph.graph import StateGraph, END
from agents.search_agent import SearchAgent
from agents.footfall_agent import FootfallAgent
from agents.analysis_agent import AnalysisAgent

from typing import Dict, Any

class CompetitorState(Dict[str, Any]):
    """Holds state data shared between graph nodes."""

def create_competitor_graph():
    builder = StateGraph(CompetitorState)  #   schema

    builder.add_node("Search", SearchAgent())
    builder.add_node("Footfall", FootfallAgent())
    builder.add_node("Analyze", AnalysisAgent())

    builder.set_entry_point("Search")
    builder.add_edge("Search", "Footfall")
    builder.add_edge("Footfall", "Analyze")
    builder.add_edge("Analyze", END)

    return builder.compile()
