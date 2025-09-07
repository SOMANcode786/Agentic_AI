import os
from dotenv import load_dotenv

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    function_tool,
    
    ModelSettings,
    RunConfig
    
)

load_dotenv()





GEMINI_API = os.getenv("GEMINI_API_KEY")
print("Api: ",GEMINI_API)

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API,
    base_url=BASE_URL,
)


model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client,
)
config=RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent=Agent(
    name="simple agent",
    instructions="you are helpful assistant give a answer to the user question",
    model_settings=ModelSettings(
        temperature=0.9,
        
        top_p=1.0
    )
)
# find the propbailty
prompt="i like to eat"
result=Runner.run_sync(agent,prompt,run_config=config)
print("Answer :" ,result)