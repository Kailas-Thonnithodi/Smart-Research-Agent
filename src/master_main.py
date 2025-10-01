from agents import Runner, trace, gen_trace_id
from src.smart_agents.searcher import search_agent
from src.smart_agents.search_optimiser import search_optimiser_agent, WebSearchTerm, WebSearchPlan
from src.smart_agents.writer import writer_agent, ReportData
from src.smart_agents.emailer import emailer_agent
import asyncio

# The Head Research Manager / Master Agent
class ResearchManager:
    async def execute(self, query: str):
        '''Execute the whole process, yielding the status updates and the final report.
        Yield will pause the program for a couple of microseconds, before executing the task at hand.'''
        trace_id = gen_trace_id()
        with trace("Research Trace", trace_id=trace_id):
            # Allows me to see Research Managers's Trace once run. 
            trace_web_location = f"http://platform.openai.com/traces/{trace_id}"
            print(f"View Trace: {trace_web_location}")
            yield f"View Trace: {trace_web_location}"

    
    async def create_search_plan(self, query: str) -> WebSearchPlan:
        '''Plan the x potential searches to perform on query during the perform_searches function.'''
        print("Creating Search Plan...")
        query = f"Query: {query}"
        plan = await Runner.run(search_optimiser_agent, query)
        print(f"Created Search Plan for {len(plan.final_output.searches)} Searches.")

    async def search(self, item: WebSearchTerm) -> str | None:
        '''Perform a search (based on websearchterms from plan_searches) for the inputted query. This will be executed x amount of times on perform_searches function.'''
        search_term = f"Search Term: {item.query}.\n Reason for using Search Term: {item.reason}"
        try:
            result = await Runner.run(search_agent, search_term)
            return str(result.final_output)
        except Exception:
            return None
    
    async def execute_searches(self, search_plan: WebSearchPlan) -> list[str]:
        '''Apply the WebSearchTool agent onto each search item in the search plan.
           The should return a list of strings (the output generate from the searcher agent) for each item.'''
        searches = 0
        total_searches = [asyncio.create_task(self.search(search_term)) for search_term in search_plan.searches]
        search_outputs = []
        for search in asyncio.as_completed(total_searches):
            # search is a asynced co-routine which will be executed (await) returning the 500 word summary of WebSearchTool Agent for each prompt. 
            search_output = await search
            if search_output is not None:
                search_outputs.append(search_output)
            searches += 1
            search_fraction = float(round(searches/len(total_searches)))
            search_percentage = float(search_fraction) * 100
            print(f"Searching ({search_percentage}%)...")
        print("Searching Completed (100%)")
        return search_outputs


    
    




