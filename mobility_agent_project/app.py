import streamlit as st
from agents.mobility_agent import run_mobility_readiness_agent
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Mobility Readiness Agent", layout="centered")
st.title("🧭 Mobility Readiness Agent")

with st.form("mobility_form"):
    preferred_locations = st.multiselect("Preferred Work Locations", ["Kerala", "Bangalore", "Delhi", "Hyderabad"])
    current_location = st.selectbox("Current Location", ["Kerala", "Bangalore", "Delhi", "Hyderabad"])
    hospital_size = st.selectbox("Preferred Hospital Size", ["Small", "Medium", "Large"])
    open_to_small = st.checkbox("Open to small/rural hospitals?", value=True)
    tech_tools = st.multiselect("Tech tools used", ["EHR", "Zoom", "MS Teams", "Telemedicine"])
    telehealth = st.checkbox("Do you have telehealth experience?", value=False)

    submitted = st.form_submit_button("Evaluate Readiness")

    if submitted:
        mobility_input = {
            "preferred_locations": preferred_locations,
            "current_location": current_location,
            "hospital_size_preference": hospital_size,
            "open_to_small_hospitals": open_to_small,
            "tech_tools_used": tech_tools,
            "telehealth_experience": telehealth
        }

        with st.spinner("🤖 Evaluating Mobility Readiness..."):
            try:
                result = run_mobility_readiness_agent(mobility_input)

                st.success("✅ Evaluation Complete!")
                st.markdown(f"```json\n{result}\n```")
            except Exception as e:
                st.error(f"❌ Error: {e}")
