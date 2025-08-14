from agents import Agent,Runner,RunContextWrapper,function_tool

from dataclasses import dataclass



@dataclass
class context:
    name: str
    description: str


@function_tool
async def 