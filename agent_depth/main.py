
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig,enable_verbose_stdout_logging
from pydantic import BaseModel
from dotenv import load_dotenv 
import os                                                                 
load_dotenv()
enable_verbose_stdout_logging()
gemini_api_key=os.getenv("GEMINI_API_KEY")
print(gemini_api_key)

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
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


# math=Agent(
#     name="Math",
#     instructions="You are a helpful math assistant. You can only answer math questions."
# )
# result=Runner.run_sync(
#     math,
#     input="What is 25 multiplied by 4",
#     run_config=config
# )

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


response=  Runner.run_sync(recipe_agent,"birynai with chicken",run_config=config)
print(response.final_output)

# print("The result is : -- > : ",result.final_output)