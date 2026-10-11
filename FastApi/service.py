import uuid

from src.researchagent.graph.graph import graph


def run_researchagent(
    question: str,
    thread_id: str | None = None
):
    if thread_id is None:
        thread_id = str(uuid.uuid4())

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    initial_state = {
        "question": question,
        "plan": "",
        "messages": [],
        "sources": [],
        "findings": "",
        "verification": "",
        "verification_decision": "",
        "research_iterations": 0,
    }

    result = graph.invoke(
        initial_state, # type: ignore
        config=config, # type: ignore
    )

    messages = result.get("messages", [])

    print("\n========== SERVICE DEBUG ==========")
    print("MESSAGE COUNT:", len(messages))

    for i, message in enumerate(messages):
        print(f"\nMESSAGE {i}")
        print("TYPE:", type(message).__name__)
        print("CONTENT:", repr(message.content))
        print("TOOL CALLS:", getattr(message, "tool_calls", None))

    print("===================================\n")

    answer = ""

    # Find the last message that actually contains text
    for message in reversed(messages):
        content = getattr(message, "content", "")

        if isinstance(content, str) and content.strip():
            answer = content
            break

    return {
        "thread_id": thread_id,
        "question": question,
        "answer": answer,
        "sources": result.get("sources", []),
        "verification": result.get("verification", ""),
    }