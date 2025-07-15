# 🤖 Gemini-Powered AI Assistant (via OpenAI-Compatible SDK)

This project demonstrates how to build a simple AI agent using the **Google Gemini API** through the **OpenAI-compatible SDK interface**. It uses an asynchronous OpenAI-like client to call the `gemini-2.0-flash` model, processes a user prompt, and prints the output.

---

## 📌 Features

- ✅ Uses **Google Gemini API** via OpenAI-compatible interface
- ⚡ Powered by the lightweight `gemini-2.0-flash` model
- 🤝 Built with an `Agent`, `Runner`, and `RunConfig` system
- 🔐 Loads API key securely using `.env` file
- 🔄 Asynchronous execution with `asyncio`

---

## 📁 Project Structure

.
├── main.py # Main agent execution file
├── .env # Environment file with your Gemini API key
└── README.md # Project documentation (this file)

yaml
Copy
Edit

---

## 🔧 Requirements

You need Python and a few libraries to run this project:

### ✅ Python Version
- Python 3.8 or higher

### 📦 Install Dependencies

```bash
pip install openai python-dotenv
Note: You must also have the custom agents module that supports Agent, Runner, AsyncOpenAI, etc.

🔐 Setup Instructions
Clone the repo or copy the code files to your local environment.

Create a .env file in the root directory:

env
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here
Run the script using:

bash
Copy
Edit
python main.py
🧠 Code Overview
python
Copy
Edit
# Load the Gemini API key from .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Set up the OpenAI-compatible client for Gemini
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Wrap Gemini model into OpenAI SDK interface
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Agent configuration
agent = Agent(
    name="Assistant",
    instructions="You are a helpful Assistant.",
    model=model
)

# Run a single prompt
result = await Runner.run(agent, "Tell me about recursion in programming.", run_config=config)
print(result.final_output)
📤 Example Output
css
Copy
Edit
Recursion in programming is a method where a function calls itself to solve smaller parts of a problem...
🔗 References
Gemini API - OpenAI-Compatible Interface

OpenAI Python SDK GitHub
