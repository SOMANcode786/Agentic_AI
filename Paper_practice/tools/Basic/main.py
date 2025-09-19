from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig, function_tool, ModelSettings
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=api,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

@function_tool
def calculateArea(length: float, width: float) -> str:
    """calculate area of rectangle"""
    area = width * length
    return f"Area = {length} x {width} = {area} square unit"
 

# "Required" means using tools is mandatory.
# "None" agent cannot use tools 
# "auto" defult agent use tool when needed

tools_user = Agent(
    name="Tool user",
    instructions="You are a helpful assistant, always use tools when available.",
    tools=[calculateArea],
    model_settings=ModelSettings(tool_choice="required")
    # model_settings=ModelSettings(tool_choice="none")
    # model_settings=ModelSettings(tool_choice="auto")
)



result = Runner.run_sync(
    tools_user,
    "What's the area of a 5x3 rectangle?",
    run_config=config
)

print(result.final_output)
