from langchain.tools import tool
from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search_competitor_data(location: str) -> str:
    """Search for nearby clothing store competitors and their footfall data."""
    query = f"clothing store competitors footfall and busy times near {location}"
    results = client.search(query=query, search_depth="advanced", max_results=5)
    return "\n".join([r["content"] for r in results["results"]])
