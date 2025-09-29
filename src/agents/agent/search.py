'''
Seach Agent
- The purpose of this agent is to do google searchs on the specified Topic (inserted by the user).
- Furthermore, the agent will use WebSearchTool (from openai). 
- This can use up to $0.015 per search, therefore optimising and being resourceful would be necessary every time making a call to this agent.
- The returned output of the file will be the result of the summary of singular search of topic (based on the webpage it "clicked on").
'''

# Libraries
from agents import Agent, WebSearchTool, Runner, trace
from agents.model_settings import ModelSettings
from dotenv import load_dotenv
import asyncio
from IPython.display import display, Markdown

# Loading gpt model
load_dotenv(override=True)

# agent instruction's parameters
instructions_params = {
    "paragraphs": 3,
    "words": 500,
    "tone": "efficient"
} 

# instruction set
instructions = f"""
You are a research assistant.\n
Given a search term, you search the web for that tern and produce a concise summary of the results.\n
The summary can be atleast {instructions_params["paragraphs"]} paragraphs, and must be around {instructions_params["words"]} words.\n
Capture the main points, Write in a {instructions_params["tone"]} tone.\n
This will be consumed by someone synthesizing a report, so it's vital you capture essense and ignore any fluff.\n
Do not include and additional commentary other than the summary itself. Thank you"
"""

# agent properties
search_agent = Agent(
    name = "Search Agent",
    instructions = instructions,
    tools = [WebSearchTool(search_context_size="low")], 
    model = "gpt-4o-mini",
    model_settings = ModelSettings(tool_choice = "required")
)

## Testing Agent
# samples_message = "Top 5 mobile games"
# with trace("Sample Search Agnent Output"):
#     result = Runner.run_sync(search_agent, samples_message)