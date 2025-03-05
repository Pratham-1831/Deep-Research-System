from workflows.research_workflow import ResearchWorkflow
from utils.logger import log

def run_research(query:str)->str:
    log.info(f"Starting research workflow for:{query}")
    workflow=ResearchWorkflow()
    results=workflow.graph.invoke({"query":query})
    log.success("Research completed successfully")
    return results["answer"]

if __name__=="__main__":
    query="Real Madrid football club legacy over the last century and now"
    print(f"Researching :{query}\n")
    result=run_research(query)
    print("\n Research Results:\n")
    print(result)