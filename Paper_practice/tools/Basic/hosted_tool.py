from agents import Agent,Runner, WebSearchTool, trace
from dotenv import load_dotenv

load_dotenv()

import asyncio




async def main():
    agent = Agent(
        name="Web searcher",
        instructions="You are a helpful agent.",
        tools=[WebSearchTool(user_location={"type": "approximate", "city": "Karachi"})],
    )

    with trace("Web search example"):
        result = await Runner.run(
            agent,
            "what is the weather in Manzoor colony",
        )
        print(result.final_output)
        # The New York Giants are reportedly pursuing quarterback Aaron Rodgers after his ...


if __name__ == "__main__":
    asyncio.run(main())