from typing import List
from agents import function_tool


from core.function_selector import select_key_functions
from core.summarizer import summarize_function
from agent_center.types import FunctionInfo


@function_tool(strict_mode=False)
def select_important_functions_tool(
    functions: List[FunctionInfo], top_n: int = 3
) -> List[FunctionInfo]:
    return select_key_functions(functions, top_n=top_n)


@function_tool(strict_mode=False)
def summarize_function_tool(function: FunctionInfo) -> str:
    return summarize_function(function)
