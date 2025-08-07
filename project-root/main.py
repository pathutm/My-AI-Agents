import streamlit as st
import os
import json
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Internal imports
from tools.pdf_parser import extract_text_from_pdf
from agents.agent_1_specialty_analyzer import create_specialty_analyzer_agent
from agents.agent_2_progression_mapper import run_career_progression_mapper

# Utility: clean Gemini-style ```json fenced blocks
def clean_json_response(raw_output) -> str:
    if hasattr(raw_output, "content"):
        raw_output = raw_output.content
    return re.sub(r"^```json\n|```$", "", raw_output.strip(), flags=re.MULTILINE).strip()

# UI setup
st.set_page_config(page_title="Specialty Evolution Coach", layout="centered")
st.title("🩺 Specialty Evolution Coach")

# Upload PDF
uploaded_file = st.file_uploader("Upload Clinical Experience (PDF)", type="pdf")

if uploaded_file:
    with open("temp_uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ PDF uploaded. Extracting and analyzing...")

    extracted_text = extract_text_from_pdf("temp_uploaded.pdf")

    if extracted_text:
        # ----------------- AGENT 1 -----------------
        with st.spinner("🔍 Agent 1: Analyzing specialty & strengths..."):
            agent1 = create_specialty_analyzer_agent()
            try:
                raw_result = agent1.invoke({"input": extracted_text})
                cleaned_result = clean_json_response(raw_result)

                specialty_data = json.loads(cleaned_result)
                st.subheader("📊 Specialty Analysis (Agent 1)")
                st.json(specialty_data)
            except Exception as e:
                st.error(f"❌ JSON parse error in Agent 1 output: {e}")
                st.text(raw_result if 'raw_result' in locals() else "No result")
                st.stop()

        # Extract career goal for Agent 2
        goals_text = extracted_text.split("Goals:")[-1].strip()

        # ----------------- AGENT 2 -----------------
        with st.spinner("🚀 Agent 2: Mapping career progression paths..."):
            try:
                result2 = run_career_progression_mapper(specialty_data, goals_text)
                cleaned_result2 = clean_json_response(result2)
                progression_paths = json.loads(cleaned_result2)

                st.subheader("📈 Career Progression Suggestions (Agent 2)")
                st.json(progression_paths)
            except Exception as e:
                st.error(f"❌ JSON parse error in Agent 2 output: {e}")
                st.text(result2 if 'result2' in locals() else "No result")

    else:
        st.error("❌ No text extracted from PDF.")
