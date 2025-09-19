from agents import guardrail

@guardrail
def safety_check(input_text: str) -> bool:
    banned_keywords = ["rm", "delete", "shutdown", "format"]
    for word in banned_keywords:
        if word in input_text.lower():
            return False
    return True
