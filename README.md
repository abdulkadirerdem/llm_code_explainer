# LLM Code Explainer

A powerful tool for automatically analyzing and explaining code functions using Large Language Models.

## Overview

LLM Code Explainer is a Python-based tool that helps developers understand code by:

- Loading code files for analysis
- Identifying the most significant functions based on metrics like fan-in/fan-out
- Generating clear, human-readable explanations for each key function
- Outputting both JSON and Markdown documentation

## Features

- **Function Selection**: Intelligently selects the most important functions in a codebase
- **Smart Summarization**: Leverages LLMs to create accurate function explanations
- **Multiple Output Formats**: Generates both machine-readable JSON and human-friendly Markdown
- **Agent-Based Interface**: Interact conversationally with the OpenAI agent to analyze code

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/llm_code_explainer.git
cd llm_code_explainer

# Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Command-Line Interface

```bash
# Basic usage with default parameters
python main.py

# Specify an input file and number of functions to analyze
python main.py --path examples/your_input.json --top_n 5
```

### OpenAI Agent Interface

```bash
# Start the interactive agent
python main_openai_agent.py --input examples/your_input.json
```

Then follow the prompts to interact with the agent.

## Input Format

The tool expects a JSON file with the following structure:

```json
{
  "file": "filename.py",
  "functions": [
    {
      "name": "function_name",
      "code": "function code as string",
      "docstring": "function docstring",
      "fan_in": 3,
      "fan_out": 2,
      "is_entry_point": false
    },
    ...
  ]
}
```

## Output

The tool generates two types of output in the `outputs` directory:

- `run_output.json`: Machine-readable JSON with function explanations
- `doc_output.md`: Human-friendly Markdown documentation

---
