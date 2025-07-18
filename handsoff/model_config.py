from agents import OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig
from dotenv import load_dotenv
import os
load_dotenv


gemini_api_key=os.getenv("GEMINI_API_KEY")

client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model=OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-2.5-flash"
)

config =RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)