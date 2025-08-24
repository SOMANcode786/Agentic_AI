from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, AsyncOpenAI, function_tool
from dotenv import load_dotenv
import os, random

# Load env variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please add it in your .env file.")

# Gemini client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Model setup
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider="gemini",
    tracing_disabled=True
)

# ---------------- TOOLS ----------------

@function_tool
def getweather(city: str) -> str:
    """Get current weather for a city."""
    return f"The weather in {city} is sunny ☀️ 25°C."

@function_tool
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """Convert currencies (mocked)."""
    rate = 280 if from_currency == "USD" and to_currency == "PKR" else 1.1
    return f"{amount} {from_currency} = {amount * rate:.2f} {to_currency}"

@function_tool
def solve_equation(equation: str) -> str:
    """Solve a math expression."""
    try:
        result = eval(equation)
        return f"The result of {equation} = {result}"
    except:
        return "❌ Invalid equation."

@function_tool
def tell_joke() -> str:
    """Return a random programming joke."""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did the function break up with the loop? It felt too repetitive 🔁.",
        "Why was the JavaScript developer sad? Because he didn’t Node how to Express himself!"
    ]
    return random.choice(jokes)

# Todo List state
todo_list = []

@function_tool
def add_task(task: str) -> str:
    """Add a task to todo list."""
    todo_list.append(task)
    return f"Task added ✅: {task}. Current list: {todo_list}"

@function_tool
def remove_task(task: str) -> str:
    """Remove a task from todo list."""
    if task in todo_list:
        todo_list.remove(task)
        return f"Task removed ❌: {task}. Remaining: {todo_list}"
    return f"Task '{task}' not found."

# ---------------- AGENT ----------------

multi_tool_agent = Agent(
    name="Multi-Tool Assistant",
    instructions="""
        You are a smart assistant. 
        - For weather → use getweather
        - For currency conversion → use convert_currency
        - For math → use solve_equation
        - For jokes → use tell_joke
        - For todo list → use add_task / remove_task
        Answer clearly after using the correct tool.
    """,
    tools=[getweather, convert_currency, solve_equation, tell_joke, add_task, remove_task]
)

# ---------------- RUN ----------------
while True:
    query = input("\nAsk me something (type 'exit' to quit): ")
    if (query.lower()| query.upper()) == "exit":
        break

    result = Runner.run_sync(multi_tool_agent, query, run_config=config)
    print("\n🤖 Assistant:", result.final_output)
