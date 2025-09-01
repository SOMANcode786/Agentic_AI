from agents import Agent, Runner, function_tool
import asyncio
import requests
from dotenv import load_dotenv

load_dotenv()

# ✅ Define a web search tool
@function_tool
def web_search(query: str) -> str:
    """
    Perform a simple web search for the given query.
    (Here we use DuckDuckGo's free search API as an example.)
    """
    url = "https://api.duckduckgo.com/"
    params = {"q": query, "format": "json"}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return "Sorry, search failed."

    data = response.json()
    if "AbstractText" in data and data["AbstractText"]:
        return data["AbstractText"]
    elif "RelatedTopics" in data and len(data["RelatedTopics"]) > 0:
        return data["RelatedTopics"][0].get("Text", "No relevant results found.")
    else:
        return "No results found."

# 🌐 Agent that can use the search tool
search_agent = Agent(
    name="Search Agent",
    instructions="Answer the user’s general knowledge questions using the web_search tool when needed.",
    tools=[web_search],
    model="gpt-4.1-mini"
)

async def main():
    question = "Who is the founder of Iqra University?"
    result = await Runner.run(search_agent, question)
    print("Final Output:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
