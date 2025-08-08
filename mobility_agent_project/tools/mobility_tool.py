from langchain.tools import tool
import json

@tool
def evaluate_mobility(input: str) -> str:
    """
    Evaluate mobility readiness based on a JSON string input.
    """
    data = json.loads(input)
    score = 0
    insights = []

    if data["current_location"] in data["preferred_locations"]:
        score += 10
    if len(data["preferred_locations"]) > 2:
        score += 20
    elif len(data["preferred_locations"]) > 1:
        score += 10
    else:
        insights.append("Limited location flexibility")

    if data["open_to_small_hospitals"]:
        score += 30
    else:
        score += 10
        insights.append("Not open to small/rural hospitals")

    if "EHR" in data["tech_tools_used"]:
        score += 20
    if data["telehealth_experience"]:
        score += 20
    else:
        insights.append("Needs telehealth training")

    result = {
        "mobility_score": min(score, 100),
        "insights": insights
    }

    return json.dumps(result, indent=2)
