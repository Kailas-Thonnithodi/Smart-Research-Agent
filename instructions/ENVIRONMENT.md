## ⚙️ Environment Setup

1. Clone the repository:
   !git clone https://github.com/Kailas-Thonnithodi/Smart-Research-Agent.git

2.	Create a .env file.
In the .env file, include the following: 
* OPENAI_API_KEY={YOUR_API_KEY}
* SENDGRID_API_KEY={YOUR_API_KEY}

3.	After setting that up, open src/local_main.py and change the query to whichever query you would like to test.

4.	Open src/smart_agents/emailer.py and update the from and to email addresses (these must match the email addresses verified under your SendGrid API key).

Once setup, you can move to local execution.

## ▶️ Local Execution

1.	Once everything is set up, create an executable local_run.sh file. Run the following in your terminal (ensure the directory is pointing to ../Smart-Research-Agent): 
chmod +x src/local_run.sh

2.	If no errors appear, run: 
./src/local_run.sh

3.	This will execute the local_main agent with your query and send the generated report to your email.

4.	If this runs successfully, you can also directly run: 
uv run local_main.py

5.	Use local_run.sh only if you make significant updates to local environment libraries or other modifications.
