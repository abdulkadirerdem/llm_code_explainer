import os
from typing import Dict
from openai import OpenAI
from dotenv import load_dotenv
from agents.prompt_templates import function_summary_prompt

load_dotenv()

client = OpenAI()


def summarize_function(fn: Dict) -> str:
    prompt = function_summary_prompt(fn)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful code summarizer."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
