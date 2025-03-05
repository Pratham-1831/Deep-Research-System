from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from config import Config

class AnswerAgent:
    def __init__(self):
        self.llm=ChatGroq(
            groq_api_key=Config.GROQ_API_KEY,
            model_name=Config.LLM_MODEL,
            temperature=Config.LLM_TEMP,
            max_tokens=Config.LLM_MAX_TOKENS

        )

    def generate_answer(self,query:str,context:str)->str:
        """Generate answer using groqs llm"""
        prompt=ChatPromptTemplate.from_template(
            "Act as a professional researcher.Answer this query:{query}\n\n"
            "Context from web research:\n{context}\n\n"
            "Structure your answer with:\n"
            "-Introduction\n-Key Findings\n-Analysis\n-Conclusion\n"
            "-Sources(cite URLs from context)\n"
            "Use markdown formatting and maintain academic rigor."


        )
        chain=prompt |self.llm
        return chain.invoke({"query":query,"context":context}).content
    