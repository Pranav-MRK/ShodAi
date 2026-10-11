from langchain_core.messages import HumanMessage

from researchagent.graph.graph import graph


def main():

    config = {
        "configurable": {
            "thread_id": "test-ollama-001"
        }
    }

    print("\n" + "=" * 80)
    print("FIRST MESSAGE")
    print("=" * 80)

    result = graph.invoke(
        {
            "question": "My research topic is RAG hallucination.",
            "plan": "",
            "messages": [
                HumanMessage(
                    content="My research topic is RAG hallucination."
                )
            ],
        }, # type: ignore
        config=config, # type: ignore
    )

    print(result["messages"][-1].content)

    print("\n" + "=" * 80)
    


if __name__ == "__main__":
    main()