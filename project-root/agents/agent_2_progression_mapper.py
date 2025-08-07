from utils.llm_config import get_gemini_llm

def run_career_progression_mapper(specialty_data: dict, goals_text: str) -> str:
    llm = get_gemini_llm()

    prompt = f"""
You are a career progression coach for clinicians.

Based on the given specialty data and career goals, suggest 3 logical career progression paths. Ensure each path has a rationale.

Respond only in JSON format like:
[
  {{
    "path": "Pulmonology → Critical Care Medicine → Tele-ICU Consultant",
    "rationale": "Leverages respiratory and ICU experience to transition into remote critical care."
  }},
  ...
]

Specialty Data:
{specialty_data}

Career Goals:
{goals_text}
"""
    response = llm.invoke(prompt)
    return response.content
