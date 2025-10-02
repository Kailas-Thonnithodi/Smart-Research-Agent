from agents import Agent

instructions = "You can convert a text body to a HTML body.\n" \
               "You care given a text body which have some markdown and you need to convert it into a HTML body with a simple,\
                clear completing layout and desirable to read by a person viewing a report."

html_formatter_agent = Agent(name="HTML Formatter", instructions=instructions, model="gpt-4o-mini")
html_formatter_tool = html_formatter_agent.as_tool(name="HTML Formatter Tool", tool_description="Converts the body of text from plain to a nice html formatting report.")