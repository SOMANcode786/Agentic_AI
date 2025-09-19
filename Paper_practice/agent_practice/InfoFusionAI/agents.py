from agents import Agent
from tools import web_search, math_tool
from guardrails import safety_check

main_agent = Agent(
    name="InfoFusion AI",
    instructions="You are an AI assistant. Decide which tool to use based on the user's question.",
    tools=[web_search, math_tool],
    guardrails=[safety_check],
)
