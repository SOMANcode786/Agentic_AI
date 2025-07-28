<<<<<<< Updated upstream
from agents import (
    Agent,                           # 🤖 Core agent class
    Runner,                          # 🏃 Runs the agent
    AsyncOpenAI,                     # 🌐 OpenAI-compatible async client
    OpenAIChatCompletionsModel,     # 🧠 Chat model interface
    function_tool,                   # 🛠️ Decorator to turn Python functions into tools
    set_default_openai_client,      # ⚙️ (Optional) Set default OpenAI client
    set_tracing_disabled,           # 🚫 Disable internal tracing/logging
)
from model_config import config

# function joke(

# )

assistant=Agent(
    name=" assistant ",
    instructions="you are a helful  assistant "
)



result=Runner.run_sync(
    assistant,
    input="What is the weather today"
  
)

print("The result is : -- > : ",result.final_output)

=======
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")
client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",  # Valid Gemini model
    openai_client=external_client
)
config = RunConfig(
    model=model,
    tracing_disabled=True
    )


>>>>>>> Stashed changes
