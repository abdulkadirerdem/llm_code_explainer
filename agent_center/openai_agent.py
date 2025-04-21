from agents import Agent
from agent_center.tools import select_important_functions_tool, summarize_function_tool

code_explainer_agent = Agent(
    name="CodeExplainerAgent",
    instructions="""
You are a smart software analysis agent.

Your goal is to:
- Analyze a list of functions from a Python file.
- Select the most important ones using the tool: select_important_functions.
- For each selected function, use the tool: summarize_function to explain what it does.

You must call the tools explicitly.
""",
    tools=[select_important_functions_tool, summarize_function_tool],
)
