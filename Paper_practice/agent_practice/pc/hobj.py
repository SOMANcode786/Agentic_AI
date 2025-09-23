from agents import Agent ,OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig,Runner,RunContextWrapper
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")



clinet=AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


model=OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=clinet
)

config=RunConfig(
    model=model,
    model_provider=clinet,
    tracing_disabled=True
)

# callble instruction

def dynamic_intruction(ctx:RunContextWrapper,agent:Agent)->str:
    return "you are an helpful assistan youre task to answer the questuin"
agent=Agent(
    name="simple agent",
    instructions=dynamic_intruction
)

print("this is the instruction",agent.instructions)
result=Runner.run_sync(agent,"where is pakistan located ? ",run_config=config)

print(result.final_output)