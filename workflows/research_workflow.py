from langgraph.graph import StateGraph,END
from typing import TypedDict,List,Dict,Any
from agents.research_agent import ResearchAgent
from agents.answer_agent import AnswerAgent
from utils.logger import log

class AgentState(TypedDict):
    query:str
    search_results:List[Dict[str,Any]]
    context:str
    answer:str
    needs_revision:bool

class ResearchWorkflow:
    def __init__(self):
        self.researcher=ResearchAgent()
        self.writer=AnswerAgent()
        self.workflow=StateGraph(AgentState)

        self.workflow.add_node("research",self.execute_research)
        self.workflow.add_node("process",self.process_results)
        self.workflow.add_node("draft",self.draft_answer)
        self.workflow.add_node("quality_check",self.quality_check)



        self.workflow.set_entry_point("research")
        self.workflow.add_edge("research","process")
        self.workflow.add_edge("process","draft")
        self.workflow.add_edge("draft","quality_check")

        self.workflow.add_conditional_edges(
            "quality_check",
            self.decide_revision,
            {"approve":END,"revise":"research"}
        )


        self.graph=self.workflow.compile()

    def execute_research(self,state:AgentState):
        log.info(f"Representing query:{state['query']}")
        return {"search_results":self.researcher.search(state["query"])}
    
    def process_results(self,state:AgentState):
        log.info("Processing search results")
      
        context="\n\n".join(
            [f"##Source{i+1}\n**URL**:{res['url']}\n**Content**:{res['content'][:500]}..." 
             for i,res in enumerate(state["search_results"])]
        )
        return {"context": context}
    
    def draft_answer(self,state:AgentState):
        log.info("Drafting answer")
        return {"answer":self.writer.generate_answer
                (
                    state["query"],
                    state["context"]
                )}
    
    def quality_check(self,state:AgentState):
        log.info("Quality checking answer")
        prompt=f"""Evaluate this answer for
        1.Completeness
        2.Source citation
        3.Logical structure
        4.Relevance to query:{state['query']}
        
        Answer:\n{state['answer']}

        Respond only with 'approve' or 'revise'"""

        response=self.writer.llm.invoke(prompt).content.lower()
        return {"needs_revision":"revise"in response}
    
    def decide_revision(self,state:AgentState):
        return 'approve' if not state["needs_revision"]else "revise"
    
    
        