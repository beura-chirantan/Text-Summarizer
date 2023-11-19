import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="textSummarizer"

list_of_files = [                            #all the files that we need are here
    ".github/workflows/.gitkeep",            #while deplyoing our project we need these
    f"src/{project_name}/__init__.py",       
    f"src/{project_name}/conponents/__init__.py",            #the first one is the folder and the second one is the file
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)        # this will return the file directory along with the file name

    #CREATING A FOLDER
    if filedir != "":       #means if the file directory is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    #CREATING A FILE
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):   #if file size is 0 then execute the followiung and this will erase everything thats in the file
        with open(filepath, 'w') as f:       #w means it is opend in writing mode
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")                                                     
  