from agents import Agent ,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")
print(gemini_api_key)
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta"
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
    ),
    handoffs=[study_coach,fitness_coach]

)
promt=input("Enter the querry --> : ")
result=Runner.run_sync(triage_agent,promt,run_config=config)
print(result.final_output)
