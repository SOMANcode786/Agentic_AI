from agents import Agent, handoff, RunContextWrapper,Runner
import asyncio
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()

class UserInput(BaseModel):
    text: str
urdu_agent = Agent(
    name="Urdu agent",
    instructions="You only speak Urdu."
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English"
)


def on_handoff(agent: Agent, ctx: RunContextWrapper[None],input_data: UserInput):
    agent_name = agent.name
    print("--------------------------------")
    print(f"Handing off to {agent_name}...")
    print(f"User input: {input_data.text}")
    print("--------------------------------")

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[
            handoff(urdu_agent, on_handoff=lambda ctx: on_handoff(urdu_agent, ctx,input_type=UserInput)),
            handoff(english_agent, on_handoff=lambda ctx: on_handoff(english_agent, ctx,input_type=UserInput))
    ],
)


async def main(input: str):
    result = await Runner.run(triage_agent, input=input)
    print(result.final_output)

     

asyncio.run(main("السلام عليكم"))