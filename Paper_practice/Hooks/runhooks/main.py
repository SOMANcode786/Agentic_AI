from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,AgentHooks,RunHooks
from agents.run import RunConfig
from  dotenv import load_dotenv
import os

load_dotenv()


gemini_api_key=os.getenv("GEMINI_API_KEY")



print(gemini_api_key)
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



class MyHooks(RunHooks):
    async def on_agent_start(self, context, agent):
        print("Agent Start:")

    async def on_agent_end(self, context, agent, output):
        print("Agent End:")



agent=Agent(
    name="Simple Agent",
    instructions="you are helpful simple agent that told the user querry with briefly"
)


result=Runner.run_sync(
    agent,
    "hi",
    hooks=MyHooks()
)


print(result.final_output)