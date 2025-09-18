# backend/agent.py
from agents import Agent, Runner, AsyncOpenAI, RunConfig, OpenAIChatCompletionsModel
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


# Define agent
assistant = Agent(
    name="SimpleAssistant",
    instructions="You are a helpful assistant. Answer the user's question briefly."
)

