'''
Emailer Agent
- The purpose of this agent is to package the contents/report produced by the writer agent, and output the email in a well structured html format.
- The email reciever should be able to view the report (from the writer agent) and have access to clickable links produced by it. Technically, it should be interactive. 
'''

# Libraries
from agents import Agent, function_tool
from dotenv import load_dotenv
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
You are an assistant that sends {instructions_params["format"]}-formatted HTML emails.

Task: Convert the provided detailed report into a single HTML email and send it using the send_email tool.  

Requirements:  
- Subject line must be clear and relevant.  
- Body must be clean, well-structured HTML.  
- Call the send_email tool once with the subject and HTML body.  
- Do not output anything else.  
"""

# A function which is used for transporting the findings in the form of a report (report being completed by the writer agent).
@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """ Send out an email with the given subject and HTML body """
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("kthonnithodi@gmail.com")
    to_email = To("kthonnithodi@gmail.com")
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content)
    mail_json = mail.get()
    response = sg.client.mail.send.post(request_body=mail_json)
    return {"status": "success"}

# agent properties
emailer_agent = Agent(
    name = "Emailer Agent",
    instructions = instructions,
    tools = [send_email], 
    model = "gpt-4o-mini"
)