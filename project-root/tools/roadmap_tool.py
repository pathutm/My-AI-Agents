from langchain.tools import tool
import json
import re

@tool
def build_career_roadmap(input: str) -> str:
    """
    Build a career roadmap based on combined input JSON.
    The `input` can be a JSON string or Python dict with keys:
    specialty_analysis, career_paths, certifications, mobility_result
    """
    try:
        # Handle both dicts and strings
        if isinstance(input, dict):
            data = input
        else:
            clean_input = str(input).strip()
            # Remove markdown code fences if present
            clean_input = re.sub(r"^```(?:json)?|```$", "", clean_input, flags=re.MULTILINE).strip()
            data = json.loads(clean_input)

        roadmap = [
            {"objective": "Expand clinical expertise",
             "key_results": ["Complete advanced fellowship in chosen specialty by Q3"]},
            {"objective": "Boost leadership skills",
             "key_results": ["Take hospital leadership training by Q4"]},
            {"objective": "Strengthen technical proficiency",
             "key_results": ["Master EHR and telehealth tools by Q2"]},
            {"objective": "Increase mobility opportunities",
             "key_results": ["Apply to 3 hospitals in preferred locations by Q1"]},
            {"objective": "Enhance academic profile",
             "key_results": ["Publish at least 1 research paper by Q4"]}
        ]

        return json.dumps({
            "roadmap": roadmap,
            "context": data
        }, indent=2)

    except Exception as e:
        return f"❌ Failed to build roadmap: {e}"
