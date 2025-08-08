import streamlit as st
import os
from dotenv import load_dotenv

# Internal imports
from tools.pdf_parser import extract_text_from_pdf
from agents.agent_1_specialty_analyzer import create_specialty_analyzer_agent
from agents.agent_2_progression_mapper import run_career_progression
from agents.agent_3_certification_rag_agent import run_certification_suggester

# Load environment variables
load_dotenv()

# Streamlit UI setup
st.set_page_config(page_title="Specialty Evolution Coach", layout="centered")
st.title("🩺 Specialty Evolution Coach")

# File upload
uploaded_file = st.file_uploader("Upload Clinical Experience (PDF)", type="pdf")

if uploaded_file:
    # Save uploaded PDF
    with open("temp_uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ PDF uploaded. Extracting and analyzing...")

    extracted_text = extract_text_from_pdf("temp_uploaded.pdf")

    if extracted_text:
        # ----------------- AGENT 1 -----------------
        with st.spinner("🔍 Agent 1: Analyzing specialty & strengths..."):
            agent1 = create_specialty_analyzer_agent()
            try:
                raw_result = agent1.run(extracted_text)
                st.subheader("📊 Specialty Analysis (Agent 1)")
                st.markdown(raw_result)
            except Exception as e:
                st.error(f"❌ Agent 1 error: {e}")
                st.text(raw_result if 'raw_result' in locals() else "No result")
                st.stop()

        # ----------------- AGENT 2 -----------------
        with st.spinner("🚀 Agent 2: Mapping career progression paths..."):
            try:
                result2 = run_career_progression(raw_result)
                st.subheader("📈 Career Progression Suggestions (Agent 2)")
                st.markdown(result2)
            except Exception as e:
                st.error(f"❌ Error in Agent 2: {e}")
                st.text(result2 if 'result2' in locals() else "No result")
                st.stop()
        
        # ----------------- AGENT 3 -----------------
if 'raw_result' in locals():
    with st.spinner("🎓 Agent 3: Suggesting Certifications..."):
        try:
            cert_result = run_certification_suggester(raw_result)
            st.subheader("🎓 Suggested Certifications (Agent 3)")
            st.markdown(cert_result)
        except Exception as e:
            st.error(f"❌ Error in Agent 3: {e}")
