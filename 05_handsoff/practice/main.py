from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, AsyncOpenAI
from dotenv import load_dotenv
import os   

# Load environment variables
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Gemini via OpenAI-compatible endpoint
external_client = AsyncOpenAI(
    api_key=gemini_api_key,

    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define Gemini model
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",   # ✅ correct model name
    openai_client=external_client,
)               
# Run configuration
config = RunConfig(
    model=model,
    model_provider="gemini",   # ✅ not "openai"
    tracing_disabled=True
)


language_agent = Agent(
    name="Language Agent",
    instructions="""
        You are a helpful language assistant.
        Your task is to answer questions related to languages.
    """
)

math_agent = Agent(
    name="Math Agent",
    instructions="""
        You are a helpful math assistant.
        Your task is to answer math questions.
    """     

)
# Triage agent with handoffs
triage_agent = Agent(
    name="Triage Agent",
    handoffs=[language_agent, math_agent]
)   

input_query = input("Enter the question: ")

# Run synchronously
result = Runner.run_sync(triage_agent, input_query, run_config=config)
print("The result is : -- > : ", result.final_output)