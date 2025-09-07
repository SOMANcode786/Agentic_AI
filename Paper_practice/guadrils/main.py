from agents import Agent ,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig,enable_verbose_stdout_logging
from dataclasses import dataclass
from dotenv import load_dotenv
import os
import asyncio
from openai.types.responses import ResponseTextDeltaEvent
load_dotenv()

# enable_verbose_stdout_logging()
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

async def main():
  essay_agent=Agent(
    name="Essay Agent",
    instructions="you are helpful education assistant youre task to write a 10 line essay about the user topic "
  )

  result = Runner.run_streamed(essay_agent, input="Please tell me 5 jokes.",run_config=config)
  async for event in result.stream_events():
        # print("Event : ",event)
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print("DATA = >   ... ",event.data.delta, end="")



if __name__ == "__main__":
    asyncio.run(main())