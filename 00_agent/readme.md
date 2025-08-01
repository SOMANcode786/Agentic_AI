# OpenAI Agents Python SDK - Roman Urdu Mein Guide

Yeh SDK aapko help karta hai aik aise AI Agent bananay mein jo tools ka use karke kaam kar sakay, jaise ke file read karna, internet se data lana, ya API call karna.

---

## ⚙️ Zaroori Concepts

### 1. Agent:
Agent aik GPT model hota hai jo sochta hai aur tool ka istemal karke tasks karta hai.

### 2. Tools:
Tools woh cheezein hain jin ka agent use karta hai. Kuch tools yeh hain:

- **CodeInterpreterTool** – Python code chalana
- **BrowserTool** – Web pe search karna
- **FileTool** – File read/write karna
- **RequestsTool** – HTTP APIs call karna
- **Custom Tools** – Aap khud bhi apna tool bana saktay hain

### 3. AgentExecutor:
Yeh agent ko chalata hai aur us ka jawab return karta hai.

---

## 📘 Simple Misal (Example)

```python
from openai import AssistantAgent, CodeInterpreterTool

agent = AssistantAgent(tools=[CodeInterpreterTool()])
response = agent.run("5 ka square kya hota hai?")
print(response)
