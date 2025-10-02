from agents import Agent, Runner, trace, function_tool

instructions = """
"""

html_formatter_agent = Agent("HTML Formatter Agent", instructions = instructions, model = "gpt-4o-mini")
html_formatter_tool = html_formatter_agent.as_tool(tool_name = "HTML Formatter Tool", tool_description = "Converts Plain text into Report-like HTML Format.")