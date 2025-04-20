from agent.model import Query
from agent.tasks import handle_task

if __name__ == "__main__":
    task = Query(
        task_type="explanation",
        prompt="What are Pydantic agents and how do they work in AI?"
    )

    result = handle_task(task)
    print("🔹 AI Agent Response:\n")
    print(result.result)
