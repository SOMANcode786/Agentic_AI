from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, Runner
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Setup Gemini client
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=client
)




# Define agent
agent = Agent(
    name="gemini_chat_agent",
    model=model,
    instructions="You are a helpful tutor. Continue conversations naturally.",
)


