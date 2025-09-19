from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,RunConfig
from agents.run import AgentRunner
import os
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
runner=AgentRunner()
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = runner.run_sync(agent, "Hello, how are you.", run_config=config)

print(result.final_output)