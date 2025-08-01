from agents import Agent,Runerr ,OpenAIChatCompletionsModel,RunConfig,AsyncOpenAI
from dotenv import load_dotenv
from dataclasses import dataclass
import os
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
class American:
    name: str
    age: int
    language: ClassVar[str] = "English"

    def eats(self):
        return "f{self.name} eats hamburgers."
    
