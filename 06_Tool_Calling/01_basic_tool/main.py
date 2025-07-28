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

