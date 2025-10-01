---
title: Smart-Research-Agent
app_file: app.py
sdk: gradio
sdk_version: 5.47.2
---
# Smart-Research-Agent

## Searcher Agent
* The purpose of this agent is to do google searchs on the specified Topic (inserted by the user).
* Furthermore, the agent will use WebSearchTool (from openai). 
* This can use up to $0.015 per search, therefore optimising and being resourceful would be necessary every time making a call to this agent.
* The returned output of the file will be the result of the summary of singular search of topic (based on the webpage it "clicked on").

## Search Optimiser Agent
* The purpose of this agent is to propose x amount of questions/concepts surrounding the topic.
* This will help stir the topic of conversion when search agent is the called, leading to more meaninful and diverse range of report summaries. 
* The returned x questions/concepts should be short and be surrounded around the original concept at hand.

## Writer Agent
* The writer agent will be responsible for creating a report (predefined word and page limits), based on the findings/summaries completed by the searcher agent.
* Since the searcher agent will be completing the searches (baesed on results proposed by the search optimiser agent), the writer agent is based on the findings conducted by the data reseached by it's children agents. 

## Emailer Agent
* The purpose of this agent is to package the contents/report produced by the writer agent, and output the email in a well structured html format.
* The email reciever should be able to view the report (from the writer agent) and have access to clickable links produced by it. Technically, it should be interactive. 