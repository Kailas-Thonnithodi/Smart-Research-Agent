'''
Seacher Agent
- The purpose of this agent is to do google searchs on the specified Topic (inserted by the user).
- Furthermore, the agent will use WebSearchTool (from openai). 
- This can use up to $0.015 per search, therefore optimising and being resourceful would be necessary every time making a call to this agent.
- The returned output of the file will be the result of the summary of singular search of topic (based on the webpage it "clicked on").
'''

# Libraries
from agents import Agent, Runner, trace, function_tool
from pydantic import BaseModel, Field
from agents.model_settings import ModelSettings
from dotenv import load_dotenv
from agent_properties import GPT_MODELS

# Loading gpt model
load_dotenv(override=True)

# agent instruction's parameters
instructions_params = {
    "page_range": [5, 10],
    "words": 2000,
    "tone": "cohesive"
} 

# instruction set
instructions = f"""
You are a senior researcher who is tasked with writing a {instructions_params["tone"]} report for a research query.\n
You will be provided with the original query, and some inital reseach conducted by a research assistant.\n
You should first come up with an outline for the report that describes the structure and flow of the report.\n
Then, generate the report and return that as your final output.\n
The final output shouldbe in markdown format, and it should be lengthy and detailed.\n
The report must {instructions_params["page_range"][0]} - {instructions_params["page_range"][1]} pages long and must be around {instructions_params["words"]} words. Thank you!
"""

# Will generate a json based strucutre based on the generate report
# This will be very helpful for the emailer agent. 
class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final report.")
    follow_up_questions: str = Field(description="Suggested topics to research further.")

# agent properties
writer_agent = Agent(
    name = "Writer Agent",
    instructions = instructions,
    model = GPT_MODELS["default"],
    output_type = ReportData
)