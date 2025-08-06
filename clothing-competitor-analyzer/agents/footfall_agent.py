class FootfallAgent:
    def __call__(self, state):
        # dummy behavior for testing
        print("🧍‍♂️ Estimating footfall for competitors...")
        state["footfall_data"] = "Estimated footfall: 2000 people/week"
        return state
