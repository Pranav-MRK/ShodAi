from langchain_core.messages import HumanMessage

from researchagent.rag.llm import get_llm

PLANNER_PROMPT = """
    You are the research planner for Shod, an AI research assistant.

    Create a simple research plan for the user's question.

    The plan should contain 3-5 clear steps.

    Focus on:
    1. What information needs to be found
    2. What research sources should be searched
    3. What evidence should be compared
    4. What should be checked before answering

    Do not answer the user's question.

    User question:
    """

def planner(state):
    print("\n🧠 PLANNER STARTED")
    llm = get_llm()

    question = state["question"]
    print("🤖 Planner calling Ollama...")
    response = llm.invoke(
        [
            HumanMessage(
                content=PLANNER_PROMPT + question
            )
        ]
    )
    print("✅ Planner finished")

    return{
        "plan": response.content
    }