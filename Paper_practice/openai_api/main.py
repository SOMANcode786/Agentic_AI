from agents import Agent, Runner, handoff
import asyncio
from dotenv import load_dotenv

load_dotenv()

billing_agent = Agent(
    name="Billing agent",
    instructions="Handle billing questions.",
    model="gpt-4.1-mini"   # 👈 specify model here
)

refund_agent = Agent(
    name="Refund agent",
    instructions="Handle refunds.",
    model="gpt-4.1-mini"   # 👈 you can use different model if needed
)

triage_agent = Agent(
    name="Triage agent",
    instructions=(
        "Help the user with their questions. "
        "If they ask about billing, handoff to the Billing agent. "
        "If they ask about refunds, handoff to the Refund agent."
    ),
    handoffs=[billing_agent, handoff(refund_agent)],
    model="gpt-4.1"   # 👈 Triage uses a stronger model
)

async def main():
    result = await Runner.run(triage_agent, "I need to check refund status.")
    print("Final Output:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
