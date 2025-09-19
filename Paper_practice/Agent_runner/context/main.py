from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,RunConfig,RunContextWrapper,function_tool
import os
from dotenv import load_dotenv
from dataclasses import dataclass
#Reference: https://ai.google.dev/gemini-api/docs/openai
load_dotenv()
gemini_api_key=os.getenv("GEMINI_API_KEY")
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


@dataclass
class BankContext:
    account_data: dict=None



account_database={
    "12345": {"name": "Alice", "balance": 1000},
    "67890": {"name": "Bob", "balance": 1500},
    "54321": {"name": "Charlie", "balance": 2000}

}


print(account_database["12345"])

@function_tool
def get_account_balance( context: RunContextWrapper[BankContext],account_id: str) -> str:
    """Fetches the account balance for a given account ID."""
    ctx=context.context
    account_info=ctx.account_data.get(account_id)
    if account_info:
            return f"Account {account_id} belongs to {account_info['name']} with a balance of ${account_info['balance']}."
    else:
            return f"Account {account_id} not found."
      

agent=Agent(
    name="Banking Assistant",
    instructions="You are a banking assistant. Use the provided tools to assist users with their banking needs.",
    tools=[get_account_balance]
)

context=BankContext(
    account_data=account_database
)
result=Runner.run_sync(
    starting_agent=agent,
    input="What is the balance of account 54321?",
    run_config=config,
    context=context
)
print(result.final_output)
