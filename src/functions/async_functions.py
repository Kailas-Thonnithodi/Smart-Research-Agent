# Libraries
from agents import Runner, trace
import asyncio
from src.smart_agents import searcher, search_optimiser, writer, emailer

async def plan_searches(query: str):
    """Calling search_optimiser to find an instance of prompt for the query"""
    print("Planning searches...")
    result = await Runner.run(search_optimiser.search_optimiser_agent, f"Query: {query}")
    print(f"Will perform {len(result.final_output.searches)} searches")
    return result.final_output

async def search(item: search_optimiser.WebSearchTerm):
    """ Use the search agent to run a web search for each item in the search plan """
    input = f"Search term: {item.query}\nReason for searching: {item.reason}"
    result = await Runner.run(searcher.searcher_agent, input)
    return result.final_output

async def perform_searches(search_plan: search_optimiser.WebSearchPlan):
    """ Calling search_optimiser to discover x amount of prompts based on the query provided."""
    print("Searching...")
    tasks = [asyncio.create_task(search(item)) for item in search_plan.searches]
    results = await asyncio.gather(*tasks)
    print("Finished searching")
    return results

async def write_report(query: str, search_results: list[str]):
    """ Use the writer agent to write a report based on the search results"""
    print("Thinking about report...")
    input = f"Original query: {query}\nSummarized search results: {search_results}"
    result = await Runner.run(writer.writer_agent, input)
    print("Finished writing report")
    return result.final_output

async def send_email(report: writer.ReportData):
    """ Use the email agent to send an email with the report """
    print("Writing email...")
    result = await Runner.run(emailer.emailer_agent, report.markdown_report)
    print("Email sent")
    return report