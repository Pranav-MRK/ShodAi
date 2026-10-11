# from researchagent.graph.planner import planner


# def main():

#     state = {
#         "question": "How can RAG reduce hallucinations in LLMs?",
#         "plan": "",
#         "messages": [],
#     }

#     result = planner(state)

#     print("\n" + "=" * 80)
#     print("SHOD RESEARCH PLAN")
#     print("=" * 80)

#     print(result["plan"])


# if __name__ == "__main__":
#     main()


# from langchain_core.messages import HumanMessage

# from researchagent.graph.graph import graph


# def main():

#     config = {
#         "configurable": {
#             "thread_id": "test-user-1"
#         }
#     }

#     print("\n" + "=" * 80)
#     print("FIRST MESSAGE")
#     print("=" * 80)

#     result = graph.invoke(
#         {
#             "question": "My research topic is RAG hallucination.",
#             "plan": "",
#             "messages": [
#                 HumanMessage(
#                     content="My research topic is RAG hallucination."
#                 )
#             ],
#         },
#         config=config,
#     )

#     print(result["messages"][-1].content)

#     print("\n" + "=" * 80)
#     print("SECOND MESSAGE")
#     print("=" * 80)

#     result = graph.invoke(
#         {
#             "question": "What is my research topic?",
#             "plan": "",
#             "messages": [
#                 HumanMessage(
#                     content="What is my research topic?"
#                 )
#             ],
#         },
#         config=config,
#     )

#     print(result["messages"][-1].content)


# if __name__ == "__main__":
#     main()



# from langchain_core.messages import HumanMessage

# from researchagent.graph.graph import graph


# def main():

#     config = {
#         "configurable": {
#             "thread_id": "test-user-1"
#         }
#     }

#     print("\n" + "=" * 80)
#     print("FIRST MESSAGE")
#     print("=" * 80)

#     result = graph.invoke(
#         {
#             "question": "My research topic is RAG hallucination.",
#             "plan": "",
#             "messages": [
#                 HumanMessage(
#                     content="My research topic is RAG hallucination."
#                 )
#             ],
#         },
#         config=config, # type: ignore
#     )

#     print(result["messages"][-1].content)

#     print("\n" + "=" * 80)
#     print("SECOND MESSAGE")
#     print("=" * 80)

#     result = graph.invoke(
#         {
#             "question": "What is my research topic?",
#             "plan": "",
#             "messages": [
#                 HumanMessage(
#                     content="What is my research topic?"
#                 )
#             ],
#         },
#         config=config, # type: ignore
#     )

#     print(result["messages"][-1].content)


# if __name__ == "__main__":
#     main()


from researchagent.database.checkpointer import get_checkpointer


def main():

    checkpointer = get_checkpointer()

    config = {
        "configurable": {
            "thread_id": "test-user-1"
        }
    }

    print("\n" + "=" * 80)
    print("CHECKING SHOD POSTGRESQL CHECKPOINTER")
    print("=" * 80)

    checkpoint = checkpointer.get(config)

    if checkpoint:
        print("Checkpoint found ✅")
        print(checkpoint)
    else:
        print("No checkpoint found yet.")
        print("PostgreSQL connection is working ✅")


if __name__ == "__main__":
    main()