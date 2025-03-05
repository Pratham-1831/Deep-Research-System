from langchain_community.tools.tavily_search import TavilySearchResults
from config import Config

class ResearchAgent:
    def __init__(self):
        self.tool=TavilySearchResults(
            max_results=Config.MAX_SEARCH_RESULTS,
            tavily_api_key=Config.TAVILY_API_KEY
        )
    
    def search(self,query:str)->list:
        """Search Web using tavily api"""
        return self.tool.invoke({"query":query})
    