import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv() 
from graph_flow.competitor_graph import create_competitor_graph

st.title("🛍️ Competitor Intelligence for Clothing Stores")
st.write("Analyze nearby clothing store competitors with AI-powered insights.")

location = st.text_input("Enter your store location (e.g., Koramangala, Bangalore)")

if st.button("Generate Report") and location:
    with st.spinner("Analyzing nearby competitors..."):
        graph = create_competitor_graph()
        final_state = graph.invoke({"location": location})
        st.success("Report generated!")
        st.markdown("### 📊 Competitor Insights")
        st.write(final_state.get("report"))
