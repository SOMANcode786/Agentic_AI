from agents import Runner
from agents import main_agent

runner = Runner()
question = "Find latest SpaceX news and calculate 3^12."
result = runner.run(main_agent, question)

print("FINAL OUTPUT:\n", result.output)