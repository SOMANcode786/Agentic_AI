from dotenv import load_dotenv
import os 
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig
from pydantic import BaseModel

load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")


client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config=RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

class Recipe(BaseModel):
    title: str
    ingredients: list[str]
    cooking_items:int
    serving: int

recipe_agent=Agent(
    name="Recipe Agent",
    instructions="you are  an agent for creating recipes . you will  be given the name   of a food and you job"
                    "is to output that as an actual  detailed recipe .The  cooking time should be in minute.",
    output_type=Recipe
)


response=  Runner.run_sync(recipe_agent,"birynai with chicken")
print(response.final_output)