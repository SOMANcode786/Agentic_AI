from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, AsyncOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

# Run configuration
config = RunConfig(
    model=model,
    model_provider="openai",  # should be a provider name string
    tracing_disabled=True
)

# Agents
customer_support = Agent(
    name="Customer Support Assistant",
    instructions="""
        You are a helpful customer support assistant.
        Your task is to answer customer support questions.
        Give responses in bullet points with brief sentences.
    """
)
progimming_education = Agent(
    name="Education Assistant",
    instructions="""
        You are a helpful progimming_educationn assistant.
        Your task is to answer questions related to progimming_education.
    """
)

# Triage agent with handoffs
triage_agent = Agent(
    name="Triage Agent",
    handoffs=[customer_support,progimming_education]
)

# Take input
query = input("Enter the question: ")

# Run synchronously
result = Runner.run_sync(triage_agent, query, run_config=config)

print(result.final_output)
