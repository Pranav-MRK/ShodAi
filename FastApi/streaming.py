import json
import uuid

from researchagent.graph.graph import graph


def stream_research(
    question: str,
    thread_id: str | None = None,
):

    if thread_id is None:
        thread_id = str(uuid.uuid4())

    config = {
        "configurable": {
            "thread_id": thread_id,
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

    # --------------------------------
    # Thread
    # --------------------------------

    yield f"data: {json.dumps({
        'type': 'thread',
        'thread_id': thread_id,
    })}\n\n"

    try:

        # --------------------------------
        # Graph stream
        # --------------------------------

        for event in graph.stream(
            initial_state, # type: ignore
            config=config, # type: ignore
            stream_mode="custom",
        ):

            yield f"data: {json.dumps(event)}\n\n"

        # --------------------------------
        # Done
        # --------------------------------

        yield f"data: {json.dumps({
            'type': 'done'
        })}\n\n"

    except Exception as error:

        print("STREAM ERROR:", error)

        yield f"data: {json.dumps({
            'type': 'error',
            'message': str(error),
        })}\n\n"