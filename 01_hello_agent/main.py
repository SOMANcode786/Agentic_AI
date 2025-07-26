from agents import Agent,Runner,OpenAIChatCompletionsModel,RunConfig
import os
from dotenv import load_dotenv

gemini_api_key=os.getenv("GEMINI_API_KEY")
external_client= AsyncOpenAI(
    api_key=gemini_api_key,
    

)
    






agent=Agent(
    name="Salam Karna wala Agent",
    instruction="you are agent youre task to salam when someone say hello hi and any ohter greeting word "
)

result=Runner.run_sync(
    agent,
    input="Hi how are you"
)

print(result.final_output)