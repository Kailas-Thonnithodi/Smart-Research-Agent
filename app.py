import gradio as gr 
from dotenv import load_dotenv
from src.master_agent import ResearchManager

load_dotenv(override=True)

async def run(query: str):
    '''Apply async for each yield stops in the run() function in ResearchManager.
       The yield shows the user the thinking process when the agent is producing the report or doing an action.'''
    async for chunk in ResearchManager().run(query):
        yield chunk

with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    '''Creating an interactive chatbot which does the following:
       1. Asks the user what topic they would like research today.
       2. If the user typed a query, they can press the run button. 
       3. If the run button is clicked, execute the run function.'''
    gr.Markdown("# Smart Research Agent")
    query_textbox = gr.Textbox(label="What topic would you like to research today?")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")
    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)