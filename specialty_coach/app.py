import streamlit as st
import tempfile
from tools.file_parser import extract_text_from_pdf
from agents.initiator import run_all_agents

st.set_page_config(page_title="Specialty Evolution Coach", layout="centered")
st.title("🧠 Specialty Evolution Coach")

uploaded_file = st.file_uploader("Upload Clinical Record (PDF)", type=["pdf"])
career_goals = st.text_area("Enter Career Goals", placeholder="e.g., Become a Tele-ICU Consultant...")

if uploaded_file and career_goals:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_path = tmp_file.name

    st.success("✅ PDF uploaded successfully!")

    clinical_text = extract_text_from_pdf(temp_path)
    st.subheader("📄 Extracted Clinical Text")
    st.text_area("Clinical Summary", clinical_text, height=250)

    if st.button("🔍 Run Specialty Evolution Coach"):
        with st.spinner("Running agents..."):
            result = run_all_agents(clinical_text, career_goals)

        st.subheader("📊 Specialty Analysis")
        st.json(result["specialty_analysis"])

        st.subheader("🚀 Career Progression Suggestions")
        st.code(result["career_progression"], language="json")
