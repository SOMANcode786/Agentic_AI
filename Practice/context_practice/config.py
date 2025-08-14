from agents import OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini_model = OpenAIChatCompletionsModel(
   
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com",


)

model=AsyncOpenAI(
    model="gemini-1.5-flash",
    opeenai_client=gemini_model)

config=RunConfig(
    model=model,
    model_provider="openai",  # should be a provider name string
    tracing_disabled=True
)
