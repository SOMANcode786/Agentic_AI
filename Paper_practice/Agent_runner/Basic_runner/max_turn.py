from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,RunConfig,function_tool,enable_verbose_stdout_logging
from agents.run import AgentRunner
import os
from dotenv import load_dotenv
enable_verbose_stdout_logging()
#Reference: https://ai.google.dev/gemini-api/docs/openai
load_dotenv()
gemini_api_key=os.getenv("GEMINI_API_KEY")
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)
runner=AgentRunner()
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=False
)


@function_tool
def getweather(location:str)->str:
    """Fetches the current weather for a given location."""
    # In a real implementation, this would call a weather API.
    return f"The current weather in {location} is sunny with a temperature of 75°F."
agent: Agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant if the queery realted to weather use the tool to get the weather information.",
    tools=[getweather],
    
    )

result = runner.run_sync(
    agent,
      "waht is weather in YK?",
        run_config=config,
        
        max_turns=1
    )
print(result.final_output)