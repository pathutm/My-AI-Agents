from langchain.tools import tool
from utils.llm_config import get_gemini_llm

@tool
def map_career_progression(text: str) -> str:
    """
    Suggests 3 career progression paths based on a doctor's specialties.
    Input: Raw string like: 'Final Answer: Dr. Priya Menon's specialties are General Medicine and Pulmonology.'
    Output: Career paths with rationale.
    """
    prompt = f"""
You are a medical career guidance assistant.

Given this doctor's specialty summary, suggest 3 logical career progression paths.
Each should have a brief rationale.

Format:
1. Path: ...
   Rationale: ...

2. Path: ...
   Rationale: ...

3. Path: ...
   Rationale: ...

Doctor Summary:
{text}
"""

    llm = get_gemini_llm()
    response = llm.invoke(prompt)
    return response.content.strip()
