## https://serper.dev/

from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = "d7decd2f849df5c2063c82a5f02737fd0847f6da"


from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()