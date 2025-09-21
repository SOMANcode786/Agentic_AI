from urllib import request
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
def get_weather(city:str)->str:
    """
    Get weather for a given city
    """
    try:
        result=request.get(
            f"http://api.weatherapi.com/v1/current.json?key=8e3aca2b91dc4342a1162608252604&q={city}"
        )
        data=result.json()
        return f"The weather in {city} is {data["current"]}"
    except Exception as e:
        return f"The current not fetch weather data due to {e}"

        
 

# "Required" means using tools is mandatory.
# "None" agent cannot use tools 
# "auto" defult agent use tool when needed

tools_user = Agent(
    name="Tool user",
    instructions="You are a helpful assistant, always use tools when available.",
    tools=[get_weather],
    model_settings=ModelSettings(tool_choice="required")
    
)



result = Runner.run_sync(
    tools_user,
    "What's the weather in karachi",
    run_config=config
)

print(result.final_output)
