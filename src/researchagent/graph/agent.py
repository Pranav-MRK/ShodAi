from langchain_core.messages import SystemMessage, AIMessage
from langgraph.config import get_stream_writer

from researchagent.rag.llm import get_llm

from researchagent.tools.research_tools import (
    arxiv_search,
    research_search,
    get_paper,
)


TOOLS = [
    arxiv_search,
    research_search,
    get_paper,
]


AGENT_SYSTEM_PROMPT = """
You are Shod, an AI research assistant.

Answer the user's research question using the research
evidence and analysis provided below.

Research plan:
{plan}

Research findings:
{findings}

Research sources:
{sources}

Rules:

- Use the provided research evidence.
- Do not invent facts.
- If evidence is insufficient, say so.
- Prefer claims supported by the sources.
- Mention important limitations or conflicting evidence.
- Give a clear answer to the user.
"""


def agent(state):

    print("\n🤖 AGENT STARTED")
    print("🤖 Generating final answer...")

    llm = get_llm()

    writer = get_stream_writer()

    system_message = SystemMessage(
        content=AGENT_SYSTEM_PROMPT.format(
            plan=state["plan"],
            findings=state.get("findings", ""),
            sources="\n\n".join(
                str(source)
                for source in state.get("sources", [])
            ),
        )
    )

    messages = [system_message] + state["messages"]

    full_response = ""

    # Tell frontend that generation started
    writer({
        "type": "status",
        "status": "generating",
        "message": "Generating final answer..."
    })

    for chunk in llm.stream(messages):

        content = getattr(chunk, "content", "")

        if not content:
            continue

        full_response += content

        # Send token to LangGraph stream
        writer({
            "type": "token",
            "content": content,
        })

    print("✅ AGENT FINISHED")

    writer({
        "type": "status",
        "status": "complete",
        "message": "Answer complete."
    })

    return {
        "messages": [
            AIMessage(content=full_response)
        ]
    }