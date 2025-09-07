from agents import Agent ,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig,RunContextWrapper,enable_verbose_stdout_logging,function_tool
from dotenv import load_dotenv
import os

load_dotenv()

# enable_verbose_stdout_logging()
gemini_api_key=os.getenv("GEMINI_API_KEY")
print(gemini_api_key)
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

@function_tool
def getWeather(city:str)->str:
    print(f"/n/n [DEBUG] the weather in {city}")
    return f"the weather in {city} is Warmy"
weather_Agent=Agent(
    name="weather Assitant",
    instructions="use tool to extract the weather ",
    tools=[getWeather]
)
fitness_coach=Agent(
    name="  Fintess Coach",
    instructions=(
        "you are a running coach .Ask 1-2 question then give a week plan"
        "keep it simple and encouraging .No medical advice ."
    )
)

study_coach=Agent(
    name="Study Coach",
    instructions=(
        "you are a study coach assistant.Ask for current routine then give a 1-week schedule"
        "keep samll step and doable"
    )
)


triage_agent=Agent(
    name="you are a triage agent",
    instructions=(
        "route the users : \n"
        "-if message is about running agent ,stamina -> handoff to Fitness coach .\n"
        "if message is about study realted ,study plan,focus,notes->handoff to study coach .\n"
        "if the user ask the querry about the weather handoff to the weather agent"
    ),
    handoffs=[study_coach,fitness_coach,weather_Agent]

)
# promt=input("Enter the querry --> : ")
print("-" *10)
result=Runner.run_sync(triage_agent,"give me a study plan for 5 days simple",run_config=config)
print(result.final_output)
print("-" *10)
print(result.last_agent.name ) 
result=Runner.run_sync(triage_agent,"give me a fitnees plan",run_config=config)
print(result.final_output)
print(result.last_agent.name ) 
print("-" *10)
result=Runner.run_sync(triage_agent,"what is the weather in karachi",run_config=config)
print(result.final_output)
print(result.last_agent.name ) 
