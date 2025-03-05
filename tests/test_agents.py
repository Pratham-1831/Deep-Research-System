import pytest
from agents.research_agent import ResearchAgent
from agents.answer_agent import AnswerAgent

class TestAgents:
    @pytest.fixture
    def research_agent(self):
        return ResearchAgent()
    
    @pytest.fixture
    def answer_agent(self):
        return AnswerAgent()
    
    def test_research_agent(self,research_agent):
        results=research_agent.search("Text query")
        assert isinstance(results,list)
        assert len(results)>0

    def test_answer_agent(self,answer_agent):
        test_context="Sample context about AI advancements"
        response=answer_agent.generate_answer("Test question",test_context)
        assert isinstance(response,str)
        assert len(response)>100