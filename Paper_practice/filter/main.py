from agents import Agent, HandoffInputData, Runner, handoff
from dotenv import load_dotenv
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig
from agents import enable_verbose_stdout_logging
import os

# enable_verbose_stdout_logging()
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
get_weather = Agent(
    name="get_weather",
    instructions="You must respond: 'Today the weather is cloudy."
)


def my_filter(data: HandoffInputData) -> HandoffInputData:

    return HandoffInputData(
        input_history=data.input_history,
        pre_handoff_items=data.pre_handoff_items,
        new_items=()
    )


handoff_weather_obj = handoff(
    agent=get_weather,
    input_filter=my_filter
)

main_agent = Agent(
    name="Assistant",
    instructions="You are helpful assistant.",
    handoffs=[handoff_weather_obj],
)


result = Runner.run_sync(
    main_agent,
    "What is the current weather in karachi.",
    run_config=config
)
print(result.final_output)