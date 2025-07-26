# 🤖 AI Agents – Handoff Series (OpenAI SDK)

This folder contains multiple hands-on projects demonstrating **agent handoffs** using the **OpenAI SDK**, without LangChain or LangGraph. Each project shows how agents can pass tasks, use tools, and manage context directly using `openai` APIs.

---

## 📂 Projects Overview

### `01_basic_handoff/`
Simple agent simulation where one function completes a task and passes it to the next using a structured prompt.



## ⚙️ Tech Stack

- ✅ **OpenAI SDK** (No LangChain)
- 🧪 Managed via **`uv`** package manager
- 🧠 Uses **Chat Completions API** with tools, function calls, and role-based messaging

---

## 🚀 How to Run (with `uv`)

1. **Install `uv` (if not already installed)**  
   [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

2. **Install dependencies**  
   Inside any subfolder (e.g., `01_basic_handoff/`):

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install openai
