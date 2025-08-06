class AnalysisAgent:
    def __call__(self, state):
        print("🔎 Analyzing competitor data...")
        state["analysis"] = "Competitor analysis done."
        return state