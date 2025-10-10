from agents import Agent, OutputGuardrailTripwireTriggered ,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig,enable_verbose_stdout_logging,input_guardrail,GuardrailFunctionOutput,RunContextWrapper,TResponseInputItem,InputGuardrailTripwireTriggered, output_guardrail
from pydantic import BaseModel
from dotenv import load_dotenv
import os


load_dotenv()

# enable_verbose_stdout_logging()



gemini_api_key=os.getenv("GEMINI_API_KEY")  

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
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




class MessageOutput(BaseModel): 
    response: str

class SensitivityCheck(BaseModel): 
    contains_sensitive_info: bool
    reasoning: str
    confidence_level: int  # 1-10 scale

# Fast guardrail agent for checking outputs
sensitivity_guardrail_agent = Agent(
    name="Privacy Guardian",
    instructions="""
    Check if the response contains:
    - Personal information (SSN, addresses, phone numbers)
    - Internal company information
    - Confidential data
    - Inappropriate personal details
    
    Be thorough but not overly sensitive to normal business information.
    """,
    output_type=SensitivityCheck,
)

@output_guardrail
async def privacy_guardrail(  
    ctx: RunContextWrapper, 
    agent: Agent, 
    output: MessageOutput
) -> GuardrailFunctionOutput:
    # Check the agent's response for sensitive content
    result = await Runner.run(
        sensitivity_guardrail_agent, 
        f"Please analyze this customer service response: {output.response}", 
        context=ctx.context
    )
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.contains_sensitive_info,
    )

# Main customer support agent with output guardrail
support_agent = Agent( 
    name="Customer Support Agent",
    instructions="Help customers with their questions. Be friendly and informative.",
    output_guardrails=[privacy_guardrail],  # Add our privacy check
    output_type=MessageOutput,
)

async def test_privacy_protection():
    try:
        # This might generate a response with sensitive info
        result = await Runner.run(
            support_agent, 
            "What's my account status for john.doe@email.com?",
            run_config=config
        )
        print(f"✅ Response approved: {result.final_output.response}")
    
    except OutputGuardrailTripwireTriggered as e:
        print("🛑 Response blocked - contained sensitive information!")
        # Send a generic response instead
        fallback_message = "I apologize, but I need to verify your identity before sharing account details."

import asyncio

asyncio.run(test_privacy_protection())