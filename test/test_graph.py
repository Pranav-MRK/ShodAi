from researchagent.graph.graph import graph

import uuid

thread_id = str(uuid.uuid4())
def main():
    question = (
        "How do we measure whether the retrieved context"
        "contains relevant information and eliminates unnecessary noise?"
    )

    initial_state = {
        "question": question,
        "plan": "",
        "messages": [],
        "sources": [],
        "findings": "",
        "verification": "",
        "research_iterations": 0,
    }

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    print("\n" + "=" * 60)
    print("STARTING SHOD RESEARCH GRAPH")
    print("=" * 60)

    result = graph.invoke(
        initial_state, # type: ignore
        config=config, # type: ignore
    )

    print("\n" + "=" * 60)
    print("FINAL RESULT")
    print("=" * 60)

    print("\nPLAN:")
    print(result.get("plan", ""))

    print("\nFINDINGS:")
    print(result.get("findings", ""))

    print("\nVERIFICATION:")
    print(result.get("verification", ""))

    print("\nSOURCES:")
    for i, source in enumerate(result.get("sources", []), start=1):

        print(f"\nSOURCE {i}")
        print(f"Title: {source.get('title')}")
        print(f"ArXiv: {source.get('arxiv_id')}")
        print(f"URL: {source.get('url')}")

        print("\nEvidence:")
        print(source.get("evidence", "")[:1000])

 


if __name__ == "__main__":
    main()