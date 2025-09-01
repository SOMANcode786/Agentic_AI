🧠 OpenAI Agent Demo

This project demonstrates how to use the OpenAI Agents SDK (Python) inside a Jupyter Notebook.
You will learn how to create an agent, add tools, and run it with the Runner.
It also shows a multi-agent handoff example (Manager agent passing queries to sub-agents).
---
📂 Folder Structure
project_root/
│── agent/
│   ├── agent_demo.ipynb   # Jupyter Notebook with Agent code
│   ├── .env               # API key stored securely
│   └── README.md          # Documentation
 
---

⚙️ Installation

Make sure you have Python 3.10+ installed. Then install dependencies:
-
pip install openai-agents-python python-dotenv


🔑 Environment Setup

Create a .env file inside the agent/ folder:

OPENAI_API_KEY=sk-your_api_key_here

--
🚀 Usage
1. Import required packages

from agents import Agent, Runner, function_tool
from dotenv import load_dotenv
import os, asyncio


🛠 Common Parameters

name → Unique name of the agent

instructions → System prompt (can be string or function)

model → LLM to be used (e.g., o3-mini)

model_settings → Controls randomness & limits (temperature, max_output_tokens, top_p)

tools → Functions your agent can call

handoffs → List of sub-agents for multi-agent orchestration

context → Pass state or dependencies into the agent loop

guardrails → Safety checks and validation for inputs/outputs

---

🔮 Next Steps

Add more tools (like search_web, get_weather)

Create agents for specific domains (BillingAgent, RefundAgent, SupportAgent)

Experiment with guardrails for safe inputs/outputs

Build a production API using FastAPI or Express.js with these agents

---