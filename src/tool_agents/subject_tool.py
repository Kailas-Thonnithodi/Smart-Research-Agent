from agents import Agent, function_tool

instructions = "Could you write a subject for the email.\n" \
               "You are given the report, you need to write a subject for an email, in order to make the report appealing to click."

subject_agent = Agent("Email Subject Writer", instructions=instructions, model="gpt-4o-mini")
subject_tool = subject_agent.as_tool("Subject Tool", tool_description="Write an appealing subject for the email.")