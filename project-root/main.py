import streamlit as st
import json
import os
from dotenv import load_dotenv

# Internal imports
from tools.pdf_parser import extract_text_from_pdf
from agents.agent_1_specialty_analyzer import create_specialty_analyzer_agent
from agents.agent_2_progression_mapper import run_career_progression
from agents.agent_3_certification_rag_agent import run_certification_suggester
from agents.mobility_agent import run_mobility_readiness_agent

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Specialty Evolution Coach", layout="centered")
st.title("🩺 Specialty Evolution Coach")

# Session states
st.session_state.setdefault("agents_done", False)
st.session_state.setdefault("raw_result", None)
st.session_state.setdefault("result2", None)
st.session_state.setdefault("cert_result", None)
st.session_state.setdefault("mobility_done", False)
st.session_state.setdefault("mobility_result", None)

# === Upload Clinical Experience PDF ===
uploaded_file = st.file_uploader("Upload Clinical Experience (PDF)", type="pdf")

if uploaded_file and not st.session_state.agents_done:
    with open("temp_uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ PDF uploaded. Extracting and analyzing...")

    extracted_text = extract_text_from_pdf("temp_uploaded.pdf")

    if extracted_text:
        # === Agent 1: Specialty Analysis ===
        with st.spinner("🔍 Agent 1: Analyzing specialty & strengths..."):
            agent1 = create_specialty_analyzer_agent()
            try:
                result = agent1.invoke(extracted_text)
                output = result.get("output") if isinstance(result, dict) else result
                st.session_state.raw_result = output
                st.subheader("📊 Specialty Analysis (Agent 1)")
                st.markdown(output)
            except Exception as e:
                st.error(f"❌ Agent 1 error: {e}")
                st.stop()

        # === Agent 2: Career Progression ===
        with st.spinner("🚀 Agent 2: Mapping career progression paths..."):
            try:
                st.session_state.result2 = run_career_progression(st.session_state.raw_result)
                st.subheader("📈 Career Progression Suggestions (Agent 2)")
                st.markdown(st.session_state.result2)
            except Exception as e:
                st.error(f"❌ Agent 2 error: {e}")
                st.stop()

        # === Agent 3: Certification Suggestions ===
        with st.spinner("🎓 Agent 3: Suggesting Certifications..."):
            try:
                st.session_state.cert_result = run_certification_suggester(st.session_state.raw_result)
                st.subheader("🎓 Suggested Certifications (Agent 3)")
                st.markdown(st.session_state.cert_result)
            except Exception as e:
                st.error(f"❌ Agent 3 error: {e}")

        st.session_state.agents_done = True

# === Agent 4: Mobility Readiness ===
if st.session_state.agents_done and not st.session_state.mobility_done:
    st.subheader("🧭 Evaluate Mobility Readiness (Agent 4)")

    with st.form("mobility_form"):
        preferred_locations = st.multiselect("Preferred Work Locations", ["Kerala", "Bangalore", "Delhi", "Hyderabad"])
        current_location = st.selectbox("Current Location", ["Kerala", "Bangalore", "Delhi", "Hyderabad"])
        hospital_size = st.selectbox("Preferred Hospital Size", ["Small", "Medium", "Large"])
        open_to_small = st.checkbox("Open to small/rural hospitals?", value=True)
        tech_tools = st.multiselect("Tech tools used", ["EHR", "Zoom", "MS Teams", "Telemedicine"])
        telehealth = st.checkbox("Do you have telehealth experience?", value=False)

        submit_mobility = st.form_submit_button("Evaluate Mobility")

    if submit_mobility:
        mobility_input = {
            "preferred_locations": preferred_locations,
            "current_location": current_location,
            "hospital_size_preference": hospital_size,
            "open_to_small_hospitals": open_to_small,
            "tech_tools_used": tech_tools,
            "telehealth_experience": telehealth
        }

        with st.spinner("🤖 Evaluating Mobility Readiness (Agent 4)..."):
            try:
                result = run_mobility_readiness_agent(mobility_input)
                output = result.get("output") if isinstance(result, dict) else result
                st.session_state.mobility_result = output
                st.session_state.mobility_done = True
                st.success("✅ Agent 4 Complete!")
                st.markdown(f"```json\n{output}\n```")
            except Exception as e:
                st.error(f"❌ Agent 4 error: {e}")

if st.session_state.mobility_done:
    st.subheader("✅ Mobility Readiness Result (Agent 4)")
    st.markdown(f"```json\n{st.session_state.mobility_result}\n```")
from agents.agent_5_roadmap_builder import run_roadmap_builder_agent

# === Agent 5: Career Roadmap Builder ===
if st.session_state.mobility_done and "roadmap_done" not in st.session_state:
    st.subheader("🗺️ Career Roadmap (Agent 5)")

    with st.spinner("🛠️ Building your personalized roadmap..."):
        try:
            roadmap_input = {
                "specialty_analysis": st.session_state.raw_result,
                "career_paths": st.session_state.result2,
                "certifications": st.session_state.cert_result,
                "mobility_result": st.session_state.mobility_result,
            }
            roadmap_result = run_roadmap_builder_agent(roadmap_input)
            st.session_state.roadmap_done = True
            st.session_state.roadmap_result = roadmap_result
            st.success("✅ Roadmap created!")
            st.markdown(roadmap_result)
        except Exception as e:
            st.error(f"❌ Agent 5 error: {e}")