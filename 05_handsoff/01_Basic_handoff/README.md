# 🤖 01 – Basic Agent Handoff (OpenAI SDK + Gemini)

This example shows how to perform a **basic multi-agent handoff** using the `agents` SDK and the **Gemini API via OpenAI-compatible interface**.

The goal is to simulate a scenario where:
- A **triage agent** decides which expert agent (Python or Next.js) should respond based on the question.
- The input is routed to the appropriate agent using `handsffs`.

---

## 📦 What’s Inside

- ✅ Uses `AsyncOpenAI` to connect to Gemini API
- ✅ Agents are created with custom instructions
- ✅ `triage_agent` delegates the task based on input
- ✅ Simple `Runner.run_sync()` to execute flow

---

## 🧠 Key Components

| Component         | Description                                              |
|------------------|----------------------------------------------------------|
| `Agent`          | Represents a helper with a role/instruction              |
| `RunConfig`      | Manages settings like model, tracing, etc.               |
| `handsffs`       | Enables agent-to-agent delegation                        |
| `Runner.run_sync`| Executes the conversation synchronously                  |

---

## 🛠️ Setup Instructions

1. **Install dependencies using `uv`**

```bash
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install agents python-dotenv





-----
https://github.com/fistasolutions/openaiagentssdk-tutorial-unicorndevelopers/tree/main/openaiagentssdktutorial/openaiagentssdk/07BasicHandsoff
---