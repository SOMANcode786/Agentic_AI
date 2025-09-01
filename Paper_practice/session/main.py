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

# ---- Chat Function (manual session memory) ----
session_memory = {}

def chat(session_id: str, user_input: str):
    # store user input
    if session_id not in session_memory:
        session_memory[session_id] = []
    session_memory[session_id].append(f"User: {user_input}")

    # send conversation history as input
    conversation = "\n".join(session_memory[session_id])
    result = Runner.run_sync(agent, conversation)

    # extract reply safely
    reply = result.output[0].content[0].text

    # save agent reply
    session_memory[session_id].append(f"Assistant: {reply}")

    return reply


# ---- Example usage ----
if __name__ == "__main__":
    session = "abc123"

    print("User: Hello!")
    print("Assistant:", chat(session, "Hello!"))

    print("\nUser: What did I just say?")
    print("Assistant:", chat(session, "What did I just say?"))
