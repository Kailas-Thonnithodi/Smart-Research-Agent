'''
Emailer Agent
- The purpose of this agent is to package the contents/report produced by the writer agent, and output the email in a well structured html format.
- The email reciever should be able to view the report (from the writer agent) and have access to clickable links produced by it. Technically, it should be interactive. 
'''

# Libraries
from agents import Agent, function_tool, trace, Runner
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from typing import Dict

# Loading gpt model
load_dotenv(override=True)

# agent instruction's parameters
instructions_params = {
    "format": "professional and nice",
} 

# instruction set
instructions = f"""
You are able to send a {instructions_params["format"]} formatted HTML email based on a detailed report.\n
You will be provided with a detailed report.\n
You should use your tool to send only one email, providing the report converted into clean, well presented HTML with an appropriate subject line.
"""

# A function which is used for transporting the findings in the form of a report (report being completed by the writer agent).
@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """ Send out an email with the given subject and HTML body """
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("kthonnithodi@gmail.com") # Change this to your verified email
    to_email = To("kthonnithodi@gmail.com") # Change this to your email
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    response = sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}

# agent properties
emailer_agent = Agent(
    name = "Emailer Agent",
    instructions = instructions,
    tools = [send_email], 
    model = "gpt-4o-mini"
)