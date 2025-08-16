from agents import Agent, OpenAIChatCompletionsModel, Runner, RunConfig, AsyncOpenAI, function_tool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Gemini API key from .env
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

# Create Gemini client using OpenAI-compatible endpoint
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

# Run config with verbose mode
config = RunConfig(
    model=model,
    verbose=True,
    tracing_disabled=True
)

# Define a tool for multiplication
@function_tool
def multiply_tool(a: int, b: int) -> int:
    """Multiply two integers and return the result."""
    return a * b

# Create agent with the tool
agent_math = Agent(
    name="Math Assistant",
    instructions="You are a helpful assistant. Use the multiply tool when needed.",
    tools=[multiply_tool]
)

# Run the agent synchronously
if __name__ == "__main__":
    result = Runner.run_sync(
        agent_math,
        "Multiply 45 and 32",
        run_config=config
    )
    print("\nFinal Output:", result.final_output)
