from agents import Agent ,Runner ,OpenAIChatCompletionsModel,RunConfig,AsyncOpenAI,function_tool
from dotenv import load_dotenv
import os

load_dotenv()


gemini_api_key=os.getenv("Gemini_api_key")
client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )


model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)


config =RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

@function_tool
def muliply_number(a:int,b:int)-> int:
    """Multiply two numbers."""
    return a*b

@function_tool
def add_number(a:int,b:int)-> int:
    """Add two numbers."""
    return a+b

agent: Agent = Agent(
    name="Assistant",  # 🧑‍🏫 Agent's identity
    instructions=(
        "You are a helpful assistant. "
        "Always use tools for math questions. Always follow DMAS rule (division, multiplication, addition, subtraction). "
        "Explain answers clearly and briefly for beginners."
    ),
    model=model,
    tools=[muliply_number,add_number],  # 🛠️ Register tools here
)
prompt = "what is 19 + 23 * 2?"
result = Runner.run_sync(agent, prompt)
print(f"Prompt: {prompt}")
print(f"Result: {result.final_output}")