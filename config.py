import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    LLM_MODEL=os.getenv("LLM_MODEL","mixtral-8x7b-32768")
    LLM_TEMP=0.1
    LLM_MAX_TOKENS=4096
    MAX_SEARCH_RESULTS=5