import streamlit as st
from utils.pdf_loader import load_pdf_text
from graph.study_graph import build_study_graph

st.set_page_config(page_title="LangGraph Study Assistant", page_icon="📘")
st.title("📘 LangGraph Study Assistant")

uploaded_file = st.file_uploader("Upload your course PDF", type=["pdf"])

if uploaded_file:
    st.info("📄 Extracting text from PDF...")
    raw_text = load_pdf_text(uploaded_file)
    st.success("✅ Text extracted successfully!")

    if st.button("Generate Summary & Quiz"):
        st.write("⏳ Generating summary and quiz...")

        try:
            graph = build_study_graph()
            result = graph.invoke({"input_text": raw_text})

            st.subheader("📌 Summary:")
            st.markdown(result["summary"])

            st.subheader("📝 Quiz Questions:")
            quiz_output = result["quiz"]

            # 🧹 Clean and split the quiz into question blocks
            if isinstance(quiz_output, str):
                questions = quiz_output.strip().split("\n\n")
            elif isinstance(quiz_output, list):
                questions = quiz_output
            elif isinstance(quiz_output, dict):
                questions = quiz_output.get("questions", [])
            else:
                questions = [str(quiz_output)]

            # 🎯 Format each question properly
            for idx, q in enumerate(questions, 1):
                st.markdown(f"**Q{idx}.** {q.strip()}")

        except Exception as e:
            st.error(f"🚨 Error: {str(e)}")
