from agents import Agent ,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig,RunContextWrapper,enable_verbose_stdout_logging
from dotenv import load_dotenv
import os

load_dotenv()

enable_verbose_stdout_logging()
gemini_api_key=os.getenv("GEMINI_API_KEY")
print(gemini_api_key)
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
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

def dynamic_intruction(ctx:RunContextWrapper,agent:Agent)->str:
    return "you are a helpful assitant your task to answer the question"


# This is bugg in the openai agent sdk code the agent name has type string but the bumber also pass 
agent=Agent(
    name="simple agent",
    instructions=dynamic_intruction
)

result=Runner.run_sync(agent,"what is the oop ?",run_config=config)
print("this is the ouptu :" ,result.final_output)