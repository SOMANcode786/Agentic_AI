from agents import function_tool
import requests

@function_tool
def web_search(query: str) -> str:
    # Example using a free API or dummy
    return f"Results for '{query}'"

@function_tool
def math_tool(expr: str) -> str:
    allowed_chars = "0123456789+-*/(). "
    if any(c not in allowed_chars for c in expr):
        return "Unsafe expression detected!"
    try:
        return str(eval(expr))
    except Exception:
        return "Error in computation"
