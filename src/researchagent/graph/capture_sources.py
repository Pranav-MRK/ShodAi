import json

from langchain_core.messages import ToolMessage


def capture_sources(state):

    print("\n📚 CAPTURE SOURCES STARTED")

    sources = []

    for message in state["messages"]:

        if not isinstance(message, ToolMessage):
            continue

        content = message.content

        if not content:
            continue

        try:
            data = json.loads(content) # type: ignore
        except (json.JSONDecodeError, TypeError):
            continue

        if not isinstance(data, dict):
            continue

        tool_sources = data.get("sources", [])

        if not isinstance(tool_sources, list):
            continue

        for source in tool_sources:

            if not isinstance(source, dict):
                continue

            arxiv_id = source.get("arxiv_id")

            # Deduplicate by paper
            if arxiv_id and any(
                existing.get("arxiv_id") == arxiv_id
                for existing in sources
            ):
                continue

            sources.append(source)

    sources = sources[:20]

    print(f"📚 Captured {len(sources)} unique sources")

    print("📚 CAPTURE SOURCES FINISHED")

    return {
        "sources": sources
    }