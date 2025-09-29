from agents import Agent, RunConfig, Runner, handoff, AsyncOpenAI, OpenAIChatCompletionsModel
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
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
print(load_dotenv())

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
    result = await Runner.run(triage_agent, "I need to check refund status.",run_config=config)
    print("Final Output:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
