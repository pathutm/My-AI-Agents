from langchain_core.runnables import Runnable
from tools.search_tool import search_competitor_data


class SearchAgent(Runnable):
    def invoke(self, state, config=None, **kwargs):
        location = state.get("location")
        result = search_competitor_data(location)
        return {"search_results": result}

