from agents import Agent ,Runner,OpenAIChatCompletionsModel,RunConfig,AsyncOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
    

)
config=RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=
)

cusotomer_support=Agent(
    name="customer support Assistant",
    instructions="""
        you are  a helpful cutomer support assitant youre task to anwser about suctomer support 
        give the reponse in bullets point
        breif sentence
    """
)

education=Agent(
    name="Education Assistant ",
    instructions="""
        you are a education helpful assiastant youre task to told a question related to education

    """
)

triage_agent=Agent(
    name="triage Agent",
    handoffs=[cusotomer_support,education]
)

querry=input("enter the question : ")

result=Runner.run_sync(triage_agent,querry)
print(result.final_output)





