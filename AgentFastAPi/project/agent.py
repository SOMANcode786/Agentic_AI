# backend/agent.py
from agents import Agent, Runner, AsyncOpenAI, RunConfig, OpenAIChatCompletionsModel,function_tool, AgentHooks
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Get Gemini or OpenAI key from .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Choose which provider you are using
if GEMINI_API_KEY:
    external_client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
elif OPENAI_API_KEY:
    external_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
else:
    raise ValueError("No API key found. Set GEMINI_API_KEY or OPENAI_API_KEY in backend/.env")

# Model adapter
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash" if GEMINI_API_KEY else "gpt-4o-mini",
    openai_client=external_client,
)

# Run config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)


# class AgentHooks():

#     async def on_start(context, assistant):
#         print(f"🕘 Agent {assistant.name} is now in charge of handling the task")
#     async def on_end(context, agent, output):
#         print(f"✅ Agent {assistant.name} completed work with result: {output}")
#     async def on_tool_start(context, assistant, tool):
#         print(f"🔨 Agent {assistant.name} is using tool: {tool.name}")

#     async def on_tool_end(context, agent, tool, result):
#         print(f"✅🔨 Agent {assistant.name} finished using {tool.name}. Result: {result}")









@function_tool
def getweather(location: str) -> str:
    """Get the current weather for a given location."""
    # Dummy implementation for illustration
    return f"The current weather in {location} is sunny with a temperature of 25°C."


# Define agent
assistant = Agent(
    name="SimpleAssistant",
    instructions="You are a helpful assistant. Answer the user's question briefly. aslo use the getweather tool to get the weather information if needed.",
    tools=[getweather],
    # hooks=AgentHooks,
)

# ✅ Async helper
async def ask_agent_async(query: str) -> str:
    result = await Runner.run(assistant, query, run_config=config)
    return result.final_output

# ✅ Sync helper (for testing without FastAPI)
def ask_agent_sync(query: str) -> str:
    result = Runner.run_sync(assistant, query, run_config=config)
    return result.final_output
