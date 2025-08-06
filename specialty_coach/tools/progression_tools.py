from langchain.tools import tool

@tool
def career_progression_tool(specialty_data: str) -> str:
    """
    Given the specialty and strengths data, suggest at least 3 logical career progression paths.
    """
    # Simulate suggestions — replace with real logic or call an LLM
    return """
    1. Pulmonology → Tele-ICU Specialist
    2. Pulmonology → Sleep Medicine Consultant
    3. Pulmonology → Respiratory Research Lead
    """
