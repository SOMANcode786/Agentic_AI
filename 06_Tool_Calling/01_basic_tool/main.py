 

from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI         

from model_config import config


agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant")
result=Runner.run_sync(
    agent=agent,
    input="What is the weather today",
    run_config=config
)

print("The result is : -- > : ",result.final_output)


