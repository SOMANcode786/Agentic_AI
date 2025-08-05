import os
from dotenv import load_dotenv
from openai import AssistantAgent, chat
from tools.student_tools import get_student_info

# Load environment variables
load_dotenv()

# Initialize agent
agent = AssistantAgent(tools=[get_student_info])

# Ask user query
query = input("Ask your question: ")
response = chat.completions.create(
    messages=[{"role": "user", "content": query}],
    agent=agent
)

print("🤖 Agent Reply:", response.choices[0].message.content)
