from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, AsyncOpenAI,function_tool
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Gemini via OpenAI-compatible endpoint
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model=OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",   # ✅ correct model name
    openai_client=external_client,
)

# Run configuration
config = RunConfig(
    model=model,
    model_provider="gemini",   # ✅ not "openai"
    tracing_disabled=True
)

@function_tool
def getweather(city: str) -> str:
    """Get the current weather for a given city."""
    # In a real implementation, this function would call a weather API.
    # Here, we'll just return a mock response.
    return f"The current weather in {city} is sunny with a temperature of 25°C."


weather_agent=Agent(
    name="Weather Agent",
    instructions="""
        You are a helpful weather assistant.
        Your task is to provide current weather information for a given city.
        Use the getweather function to fetch the weather data.
    """,
    tools=[getweather]
)



input_query = input("Enter the city name to get the current weather: ")

result=Runner.run_sync(weather_agent,input_query,run_config=config)
print("The result is : -- > : ", result.final_output)