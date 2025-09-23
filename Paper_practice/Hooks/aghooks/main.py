from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,AgentHooks
from agents.run import RunConfig
from  dotenv import load_dotenv
import os

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


class AgentHooks():

    async def on_start(ctx,agent):
     print("on agent start")
    
    async def on_end(ctx,agent,output):
      print("AGent hooks end")
    async def on_handoff(ctx,agent,source):
      print("agent handogg")
    async def on_tool_start(ctx,agent,tool):
      print("tool calling")
    async def on_tool_end(ctx,agent,tool,result):
      print("tool end")
     
    
agent=Agent(
    name="simple",
    instructions="you are a helpful assitant ",
    hooks=AgentHooks
)


result=Runner.run_sync(
    agent,
    "what is the weather in karachi",
    run_config=config
)


print(result.final_output)