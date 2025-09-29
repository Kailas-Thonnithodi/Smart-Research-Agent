'''
Seach Optimiser Agent
- The purpose of this agent is to propose x amount of questions/concepts surrounding the topic.
- This will help stir the topic of conversion when search agent is the called, leading to more meaninful and diverse range of report summaries. 
- The returned x questions/concepts should be short and be surrounded around the original concept at hand.
'''
# Libraries
from agents import Agent, Runner, trace
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Loading gpt model
load_dotenv(override=True)

# Agent instruction's parameters
# Due to the costs of using WebSearchTool, i will use only 3 searchs. 
instructions_params = {
    "terms": 3,
} 

# instruction set
instructions = f"""
You are a optimiser research assistant.\n
Given a query, generate a set of web searches to perform to best answer the original query.\n
Output {instructions_params["terms"]} terms to query for. Thank you!"
"""

# Using the Pydantic Functions as an easier way to package json scripts. 

# Give the reasoning for picking the term, based on the query
class WebSearchTerm(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")

# This class will store the list of the x questions/concepts.
class WebSearchPlan(BaseModel):
    searches: list[WebSearchTerm] = Field(description="A list of web searches to perform to best answer the query.")

# agent properties
search_optimiser_agent = Agent(
    name = "Search Optimiser Agent",
    instructions = instructions,
    model = "gpt-4o-mini",
    output_type = WebSearchPlan
)

# Testing Agent
samples_message = "Top 5 mobile games 2025"
with trace("Sample Search Optimiser Agent Output"):
    result = Runner.run_sync(search_optimiser_agent, samples_message)