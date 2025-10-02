'''
Writer Agent
- The writer agent will be responsible for creating a report (predefined word and page limits), based on the findings/summaries completed by the searcher agent.
- Since the searcher agent will be completing the searches (baesed on results proposed by the search optimiser agent), the writer agent is based on the findings conducted by the data reseached by it's children agents. 
'''

# Libraries
from agents import Agent
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Loading gpt model
load_dotenv(override=True)

# agent instruction's parameters
instructions_params = {
    "page_range": [6, 8],
    "words": 1000,
    "tone": "cohesive"
} 

# instruction set
instructions = f"""
You are a senior researcher.

Task: Write a {instructions_params["tone"]} research report based on a query and initial research.  

Steps:  
1. Create a clear outline showing the structure and flow.  
2. Write the full report in markdown format.  

Requirements:  
- Length: {instructions_params["page_range"][0]}–{instructions_params["page_range"][1]} pages (~{instructions_params["words"]} words).  
- Style: Detailed, thorough, and structured.  
- Output only the outline and the final markdown report (no extra commentary).  
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
    model = "gpt-4o-mini",
    output_type = ReportData
)