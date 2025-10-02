'''
Seacher Agent
- The purpose of this agent is to do google searchs on the specified Topic (inserted by the user).
- Furthermore, the agent will use WebSearchTool (from openai). 
- This can use up to $0.015 per search, therefore optimising and being resourceful would be necessary every time making a call to this agent.
- The returned output of the file will be the result of the summary of singular search of topic (based on the webpage it "clicked on").
'''

# Libraries
from agents import Agent, WebSearchTool
from agents.model_settings import ModelSettings
from dotenv import load_dotenv

# Loading gpt model
load_dotenv(override=True)

# agent instruction's parameters
instructions_params = {
    "paragraphs": 3,
    "words": 300,
    "tone": "efficient"
} 

# instruction set
instructions = f"""
You are a research assistant.

Task: Search the web for the given term and write a summary.  
Length: {instructions_params["paragraphs"]} paragraphs, about {instructions_params["words"]} words.  
Tone: {instructions_params["tone"]}.  

Guidelines:  
- Focus only on key findings and main points.  
- Exclude fluff, filler, or personal commentary.  
- Output only the summary text.  
"""

# agent properties
searcher_agent = Agent(
    name = "Searcher Agent",
    instructions = instructions,
    tools = [WebSearchTool(search_context_size="low")], 
    model = "gpt-4o-mini",
    model_settings = ModelSettings(tool_choice = "required")
)