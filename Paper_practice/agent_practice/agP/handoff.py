from agents import Agent ,OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig,Runner,RunContextWrapper,enable_verbose_stdout_logging, function_tool, handoff
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

enable_verbose_stdout_logging()

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
    tracing_disabled=False
)
python_Agent=Agent(
    name="python Assistant"
)

def on_handoff(ctx:RunContextWrapper):
    print(f"Handoff Called")


python=handoff(
    python_Agent,
    on_handoff=on_handoff
    
)




agent=Agent(
    name="Math Agent",
    instructions="you task to delogate task  if task about python if  question not realted to python asnwer own  ",
    handoffs=[python]
)

result=Runner.run_sync(agent,"waht is decorater",run_config=config)
print(result.final_output)
print(result.last_agent)