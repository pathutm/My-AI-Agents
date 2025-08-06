SPECIALTY_ANALYSIS_PROMPT = """
You are an expert medical career AI assistant.

Given a healthcare professional’s clinical experience, extract:
1. Primary specialty
2. Strength orientation (Diagnostic / Surgical / Procedural / Preventive)
3. Key clinical procedures or skills mentioned

Format the output as JSON:
{{
  "primary_specialty": "...",
  "strength_orientation": "...",
  "key_skills": ["...", "..."]
}}

Input clinical data:
{input_text}
"""
