from agents import Agent ,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig,RunContextWrapper,enable_verbose_stdout_logging,function_tool,ModelSettings
from dataclasses import dataclass
from dotenv import load_dotenv
import os
import asyncio
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


@dataclass
class UserInfo:  
    name: str
    uid: int

# A tool function that accesses local context via the wrapper
@function_tool
async def fetch_user_name(wrapper: RunContextWrapper[UserInfo]) -> str:
    """Fetches only the user's name from context."""
    return f"The user's name is {wrapper.context.name}"


@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    """Fetches only the user's age from context."""
    return f"The user is 47 years old"

async def main():
    # Create your context object
    user_info = UserInfo(name="John", uid=123)  

    # Define an agent that will use the tool above
    agent = Agent[UserInfo](
    name="Assistant",
    tools=[fetch_user_name, fetch_user_age],
    model_settings=ModelSettings(
         parallel_tool_calls=False
    )
      )


    # Run the agent, passing in the local context
    result = await Runner.run(
        starting_agent=agent,
        input="What is the age and the name of user",
        context=user_info,
        run_config=config
    )

    print(result.final_output)  # Expected output: The user John is 47 years old.

if __name__ == "__main__":
    asyncio.run(main())