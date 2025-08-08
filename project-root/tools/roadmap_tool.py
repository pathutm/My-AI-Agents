from langchain.tools import tool
import json

@tool
def build_career_roadmap(input: str) -> str:
    """
    Build a career roadmap based on prior agent outputs.
    Input must be a JSON string with:
    {
        "specialty_analysis": "...",
        "career_paths": "...",
        "certifications": "...",
        "mobility_result": "..."
    }
    """

    try:
        data = json.loads(input)
    except Exception as e:
        return f"❌ Invalid input JSON: {e}"

    roadmap = f"""### 📅 Personalized Career Roadmap

1. **Objective**: Enroll in {data["certifications"].splitlines()[0]}  
   - **Key Result**: Complete by Q3  
   - **Reason**: Address skill gaps in specialty: {data["specialty_analysis"][:50]}...

2. **Objective**: Explore roles in {data["career_paths"].split()[0]} or similar areas  
   - **Key Result**: Apply by Q4  
   - **Reason**: Matches career path potential and strengths

3. **Objective**: Take on telehealth pilot responsibilities  
   - **Key Result**: Lead session by next 3 months  
   - **Reason**: Based on mobility insights & tech exposure

4. **Objective**: Attend workshop on advanced procedures  
   - **Key Result**: Complete by Q1  
   - **Reason**: Deepen expertise in {data["specialty_analysis"].split()[0]} field

5. **Objective**: Prepare application for higher role or fellowship  
   - **Key Result**: Submit by Q2  
   - **Reason**: Based on mobility readiness score & certification path

---

🎯 Total Readiness: {json.loads(data["mobility_result"])['mobility_score']}%
✅ Stay consistent and keep tracking progress every quarter.
"""

    return roadmap
