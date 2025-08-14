from agents import Agent,Runner,RunContextWrapper,function_tool

from dataclasses import dataclass



@dataclass
class context:
    name: str
    description: str


@function_tool
async def fetch_user_age(wrappert: RunContextWrapper[context]) -> int:
    return f"user {wrappert.context.name} is 30 years old."

async def main():
    user_context = context(name="Alice", description="A user interested in AI agents.")

    agent=Agent(
        name="user context agent",
        instructions="You are an agent that uses user context to provide personalized responses.",
        tools=[fetch_user_age],
        context=user_context
    )

    result=await Runner.run_async(
        agent,
        "What is my age?",
        run_context=RunContextWrapper(context=user_context)
    ) 


    print(f"User's age: {result.final_output}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
else:
    print("This script is intended to be run directly.")