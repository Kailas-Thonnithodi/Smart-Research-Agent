from src.functions import async_functions
from agents import trace
import asyncio

query = "NVDA Earnings, Income statements, balance sheets from start of 2025 to end of 2025."

async def main(query: str):
    with trace("Research trace"):
        print("Starting research...")
        search_plan = await async_functions.plan_searches(query)
        search_results = await async_functions.perform_searches(search_plan)
        report = await async_functions.write_report(query, search_results)
        await async_functions.send_email(report)  

asyncio.run(main(query))