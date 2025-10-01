from agents import Runner, trace, gen_trace_id
from src.functions import async_functions
from src.smart_agents.searcher import search_agent
from src.smart_agents.search_optimiser import search_optimiser_agent, WebSearchTerm, WebSearchPlan
from src.smart_agents.writer import writer_agent, ReportData
from src.smart_agents.emailer import emailer_agent
import asyncio