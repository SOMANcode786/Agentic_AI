from agents import Agent, MaxTurnsExceeded, ModelBehaviorError, ModelSettings, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,RunConfig,function_tool
import os
import types
from dotenv import load_dotenv

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
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)



@function_tool
def weatherTool(loc:str)->str:
    """Give the weahter """
    print(f"The weather in {loc} is sunny")


agent: Agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant if question realted to weather fetch the info from tool",
    model_settings=ModelSettings(
        tool_choice="weatherTool"
    )
    # tools=[weatherTool]
      )


try:
    result = Runner.run_sync(agent, "whta is the weather in karachi", run_config=config,max_turns=1)

    print(result.final_output)

except Exception  as mbe:
    print(f"Model Beahviour error eception is reiases -- > {types(mbe).__name__} -")