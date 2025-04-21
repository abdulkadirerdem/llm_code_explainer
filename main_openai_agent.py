import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI
from agents import Runner
from core.input_loader import load_dummy_input
from agent_center.openai_agent import code_explainer_agent

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

OpenAI.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the OpenAI Agent with a prompt and input file."
    )
    parser.add_argument(
        "--input",
        type=str,
        default="examples/dummy_input.json",
        help="Path to dummy input JSON",
    )

    args = parser.parse_args()

    print(
        "🧠 Give a task to the Agent, for example:"
        "\n- What does this agent do?"
        "\n- Analyze and explain the most important functions in the file. File path: examples/dummy_input.json"
        "\n- Scan the examples/dummy_input.json file and comment on the functions."
    )
    user_input = input("📝 Prompt: ")

    result = Runner.run_sync(code_explainer_agent, user_input)

    print("\n✅ Final Output:\n")
    print(result.final_output)
