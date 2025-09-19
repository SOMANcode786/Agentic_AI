from agents import Agent, Runner, handoff, RunContextWrapper
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

# --- Define schema (simple rakha for working demo)
class Structure(BaseModel):
    answer: str

# --- Plan Agent
plan_Agent = Agent(
    name="Plan Agent",
    instructions="You are a simple plan management agent. Answer only questions related to planning."
)

# --- Callback function for handoff
def plan_transfer(ctx: RunContextWrapper[None], input_data: Structure):
    print(f"\n[CALLBACK] Plan Agent handoff triggered with answer: {input_data.answer}")

# --- Main Agent
simple_agent = Agent(
    name="Simple Agent",
    instructions="You are a helpful assistant. If the task is about planning, handoff to Plan Agent.",
    handoffs=[
        handoff(
            agent=plan_Agent,
            tool_name_override="Plan_Assistant",
            on_handoff=plan_transfer,
            input_type=Structure
        )
    ]
)

# --- Runner test
print("------ TEST 1: Normal Question ------")
result1 = Runner.run_sync(simple_agent, "Hello, how are you?")
print("Final Agent:", result1.last_agent.name)
print("Response:", result1.final_output)

print("\n------ TEST 2: Planning Question ------")
result2 = Runner.run_sync(simple_agent, "Give me a plan for learning Java in 15 days")
print("Final Agent:", result2.last_agent.name)
print("Response:", result2.final_output)
