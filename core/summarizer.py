import os
from typing import Dict
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def summarize_function(fn: Dict) -> str:
    prompt = f"""
You are an expert Python developer and technical writer.

Analyze the following function and explain its purpose in simple terms.
Only write the explanation. Do not repeat the code.

---

Function Name: {fn['name']}
Docstring: {fn.get('docstring', 'N/A')}
Fan-in: {fn.get('fan_in')}
Fan-out: {fn.get('fan_out')}
Entry Point: {fn.get('is_entry_point')}

Code:

{fn['code']}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful code summarizer."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
