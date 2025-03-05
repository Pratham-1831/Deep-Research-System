import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

list_of_files=[
    ".env",
    "setup.py",
    "main.py",
    "config.py",

    "agents/__init__.py",
    "agents/research_agent.py",
    "agents/answer_agent.py",

    "workflows/__init__.py",
    "workflows/research_workflow.py",

    "utils/__init__.py",
    "utils/logger.py",

    "research/trials.ipynb",
    "tests/test_agents.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory;{filedir}for the file:{filename}")

    if(not os.path.exists(filepath))or(os.path.getsize(filepath)==0):
        with open(filepath,"w")as f:
            pass
            logging.info(f"Creating empty file:{filepath}")

    else:
        logging.info(f"{filename}is already existing")    
