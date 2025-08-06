from tools.file_parser import extract_text_from_pdf
from agents.initiator import run_all_agents

def main():
    file_path = "your_uploaded_pdf.pdf"
    career_goal = "Become a critical care specialist in a tele-ICU environment."

    clinical_text = extract_text_from_pdf(file_path)
    result = run_all_agents(clinical_text, career_goal)

    print("Specialty & Strength Analysis:\n", result["specialty_analysis"])
    print("\nCareer Progression Paths:\n", result["career_progression"])

if __name__ == "__main__":
    main()
