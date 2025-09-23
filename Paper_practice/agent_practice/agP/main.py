from agents import Agent ,OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig,Runner,RunContextWrapper, function_tool,enable_verbose_stdout_logging
from dotenv import load_dotenv
import os

load_dotenv()
enable_verbose_stdout_logging()
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

@function_tool

def calculator(a:int,b:int):
    """Calculate the a * b if user input the number"""
    mul=a*b
    print("Hellow World")
    return f"Multiply {a} x { b} is = {mul}"



agent=Agent(
    name="Math Agent",
    instructions="if the user question about multiply two number use the calculator method to solve the user problem ",
    tools=[calculator]
)

result=Runner.run_sync(agent,"waht is 23 multipyly  45",run_config=config)
print(result.final_output)