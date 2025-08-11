from langchain.tools import tool
import json

@tool
def build_career_roadmap(input: str) -> str:
    """
    Build a career roadmap based on combined input JSON.
    The `input` should be a JSON string with keys:
    specialty_analysis, career_paths, certifications, mobility_result
    """
    try:
        data = json.loads(input)

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
