import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,RunConfig

from pydantic import BaseModel
load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")

client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)


class MathOperation(BaseModel):
    a: int
    b: int

assistant=Agent(
    name="MathAssistant",  # 🧑‍🏫 Agent's identi
    instructions=
        "You are a helpful assistant. "
        "extract the math operation from the question and perform it using the appropriate tool. ",
    output_type=MathOperation
)
result=Runner.run_sync(
    assistant,
    "what is 19 + 23 * 2?",
    run_config=config
)


print(f"Prompt: what is 19 + 23 * 2? : {result.final_output}")