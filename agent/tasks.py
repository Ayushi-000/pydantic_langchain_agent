from agent.model import Query, Response
from agent.logic import get_llm

llm = get_llm()

def handle_task(query: Query) -> Response:
    prompt = f"Perform this task: {query.task_type}\nPrompt: {query.prompt}"
    answer = llm.invoke(prompt)
    return Response(result=answer)
