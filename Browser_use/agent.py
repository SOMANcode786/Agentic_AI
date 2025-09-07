import asyncio
from browser_use import Agent, ChatGoogle, Browser

# Chrome ko manually debug mode me chalana hoga (tum already kar chuke ho)
browser = Browser(
    executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    user_data_dir="C:\\ChromeDebug"
)

agent = Agent(
    task='Visit https://duckduckgo.com and search for "browser-use founders"',
    browser=browser,
    llm=ChatGoogle(model="gemini-2.5-flash")
)

async def main():
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
