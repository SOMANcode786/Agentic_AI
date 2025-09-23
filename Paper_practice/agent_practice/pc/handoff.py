from agents import Agent ,Runner,RunConfig,OpenAIChatCompletionsModel,AsyncOpenAI
from dotenv import load_dotenv 

import os


load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")


client=AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

external=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config=RunConfig(
    model=external,
    model_provider=external,
    tracing_disabled=True
)

cusotmer_support=Agent(
    name="customer Support ",
    instructions= "you are customer support agent your task to only anwrt related to custommer support"
)

education=Agent(
    name="eduacation ",
    instructions="you are a helpful educatio  assitant your task to answer the question related to education "
)
triage_Agent=Agent(
    name="Triage_Agent",
    instructions="you are a helpful assistant use handoff to delgate task to specialize agent",
    handoffs=[cusotmer_support,education]
)

result=Runner.run_sync(
    triage_Agent,
    "what is python",
    run_config=config
)


print(result.final_output)
print(result.last_agent)