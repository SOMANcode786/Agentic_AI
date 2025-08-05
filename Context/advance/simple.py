from dataclasses import dataclass
from agents import Agent, Task, TaskStep, TaskStatus, Runner
import asyncio

# Step 1: Context class
@dataclass
class UserContext:
    name: str
    is_pro_user: bool
    question_count: int = 0

    def can_ask(self):
        return self.is_pro_user or self.question_count < 3

    def record_question(self):
        self.question_count += 1


# Step 2: Simple Agent
class MySimpleAgent(Agent[UserContext]):
    async def run(self, step: TaskStep[UserContext]) -> TaskStep[UserContext]:
        context = step.context

        if not context.can_ask():
            return step.with_output(
                "🚫 Free limit reached. Please upgrade to Pro!", 
                status=TaskStatus.DONE
            )

        # Dummy AI response (you can replace this with OpenAI response later)
        user_question = step.input
        context.record_question()
        response = f"🤖 AI: You asked '{user_question}'. Here's a dummy response."

        return step.with_output(response)


# Step 3: Run the agent
async def main():
    name = input("👤 Enter your name: ")
    is_pro_input = input("💎 Are you a Pro user? (yes/no): ").lower()
    is_pro_user = is_pro_input == "yes"

    context = UserContext(name=name, is_pro_user=is_pro_user)
    agent = MySimpleAgent()
    runner = Runner(agent)

    while True:
        question = input("❓ Ask your question: ")
        task = Task(input=question, context=context)
        result = await runner.run(task)
        print(result.output)

        if result.status == TaskStatus.DONE:
            break

# Step 4: Run with asyncio
if __name__ == "__main__":
    asyncio.run(main())
