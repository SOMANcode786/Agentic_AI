from agents import Agent, Runner, handoff, RunContextWrapper
from agents.schema import HandoffInputData

# Define target agent
faq_agent = Agent(
    name="FAQ Agent",
    instructions="Answer only FAQ related questions."
)

# Inspect what is being handed off
def inspect_handoff(ctx: RunContextWrapper[None], input_data: HandoffInputData):
    print("\n--- HANDOFF OCCURRED ---")
    print("Conversation handed over to FAQ Agent:")
    for msg in input_data.conversation:
        print(" ", msg)
    print("-------------------------\n")

# Handoff without filter
handoff_obj = handoff(
    agent=faq_agent,
    on_handoff=inspect_handoff
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="If the question is FAQ related, handoff to FAQ Agent.",
    handoffs=[handoff_obj]
)

result = Runner.run_sync(triage_agent, "What is your refund policy?")
print("\nFinal Answer:", result.final_output)
print("Last Agent:", result.last_agent.name)
