from langchain.tools import tool

@tool
def parse_specialty_experience(input: str) -> str:
    """Parses clinical experience and returns structured specialty data."""
    return input  # Dummy tool (not used in current setup)
