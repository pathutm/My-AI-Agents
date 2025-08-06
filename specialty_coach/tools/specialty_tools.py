import os
import json
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

@tool
def specialty_strength_tool(text: str) -> str:
    """Extracts the medical specialty and strengths from a clinical profile."""
    # Stubbed response (replace with actual LLM logic if needed)
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
