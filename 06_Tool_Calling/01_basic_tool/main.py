from agents import Agent, Runner
from model_config import config



assistant=Agent(
    name=" assistant ",
    instructions="you are a helful  assistant "
)


result=Runner.run_sync(
    assistant,
    input="What is the weather today",
    run_config=config
)

print("The result is : -- > : ",result.final_output)

