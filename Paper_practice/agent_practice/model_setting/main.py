import os
from dotenv import load_dotenv

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    function_tool,
    set_tracing_disabled,
    ModelSettings
)

# 🌿 Load environment variables
load_dotenv()

# 🚫 Disable tracing
set_tracing_disabled(disabled=True)

# 🔐 API setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

# 🧠 Model (but will only be used for reasoning, not answering directly)
model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client,
)

# ---------------------- TOOLS ----------------------

@function_tool
def getweather(city: str) -> str:
    """Get the weather for a given city"""
    return f"The weather in {city} is sunny."

@function_tool
def websearch(query: str) -> str:
    """Do a web search (dummy implementation)"""
    if "prime minister" in query.lower() and "pakistan" in query.lower():
        return "The Prime Minister of Pakistan is Shehbaz Sharif."
    return f"No result found for: {query}"



agent = Agent(
    name="tool_only_agent",
    instructions=(
        "You are a helpful assistant. "
        "Always use the available tools to answer questions. "
        # "Do not answer from your own knowledge. "
        # "If no tool matches, reply with 'I don’t have a tool for that'."
    ),
    tools=[getweather, websearch],
    model_settings=ModelSettings(
        temperature=0.4
    ),
    model=model,
)


# # Low temperature (0.1) = Very focused, consistent answers
# agent_focused = Agent(
#     name="Math Tutor",
#     instructions="You are a precise math tutor.",
#     model_settings=ModelSettings(
#         tool_choice="required",
#         temperature=0.1
#         )
# )

# # High temperature (0.9) = More creative, varied responses
# agent_creative = Agent(
#     name="Story Writer",

#     instructions="You are a creative storyteller.",
#     model_settings=ModelSettings(
#         tool_choice="required",
#         temperature=0.9)
# )
# ---------------------- RUN ----------------------

result = Runner.run_sync(agent, "Who is the Prime Minister of Pakistan?")
print("Answer:", result.final_output)

result2 = Runner.run_sync(agent, "What is the weather in Lahore?")
print("Answer:", result2.final_output)

result3 = Runner.run_sync(agent, "waht is python")  # ❌ No tool available
print("Answer:", result3.final_output)



