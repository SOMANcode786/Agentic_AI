from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables
load_dotenv()

# Load GEMINI_API_KEY
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Validate API key
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in your .env file.")

# ✅ FIXED: Correct base_url for Gemini OpenAI-compatible endpoint
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define the chat model
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",  # Valid Gemini model
    openai_client=external_client
)

# Run config
config = RunConfig(model=model, tracing_disabled=True)

# Agents
python_agent = Agent(
    name="Python_Assistant",
    instructions="You are a helpful Python assistant.",
    model=model
)

next_js_agent = Agent(
    name="NextJS_Assistant",
    
    instructions="You are a helpful Next.js assistant.",
    model=model
)

triage_agent = Agent(
    name="Triage_Agent",
    instructions="Route the question to the right assistant.",
    model=model,
    handoffs=[python_agent, next_js_agent]
)

# Run the agent
async def main():
    print("🔁 Running triage agent...")
    result = await Runner.run(
        triage_agent,
        input="What is routing in Next.js?",
        run_config=config
    )
    print("✅ Run completed")
    print(result.final_output)
    print("---")
    print("NAME",triage_agent.name)

asyncio.run(main())
