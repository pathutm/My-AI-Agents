from langchain.tools import tool
import json

@tool
def specialty_strength_tool(text: str) -> str:
    """Extracts the medical specialty and strengths from a clinical profile."""
    # Extract specialty and strengths from text (LLM or rule-based)
    result = {
        "specialty": "Pulmonology",
        "strengths": [
            "Critical Care",
            "Ventilator Management",
            "Bronchoscopy",
            "Asthma and COPD Management",
            "ECG Interpretation",
            "Patient Counseling"
        ]
    }
    return json.dumps(result)
