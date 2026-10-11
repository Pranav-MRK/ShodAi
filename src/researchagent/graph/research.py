from langchain_core.messages import HumanMessage,SystemMessage

from researchagent.rag.llm import get_llm

from researchagent.tools.research_tools import(
    arxiv_search,
    research_search,
    get_paper,
)

RESEARCH_TOOLS =[
    arxiv_search,
    research_search,
    get_paper
]

RESEARCH_PROMPT = """
You are the research worker inside Shod.

Your job is to gather reliable research evidence for the user's question.

Research question:
{question}

Research plan:
{plan}

Available tools:

- arxiv_search:
  Find relevant research papers.

- research_search:
  Search Shod's existing research knowledge base.

- get_paper:
  Inspect a specific indexed paper.

Instructions:

1. Start with the most useful research tool.
2. Examine the returned evidence carefully.
3. Do NOT repeat a search query that has already been executed.
4. If previous evidence is sufficient, STOP researching.
5. If evidence is insufficient, formulate a DIFFERENT search query
   targeting the missing information.
6. Prefer relevant evidence over simply collecting more evidence.
7. Do not invent research findings.
8. Your job is to collect evidence, NOT write the final answer.
"""


def researcher(state):

    print("\n🔎 RESEARCHER STARTED")

    iteration = state.get("research_iterations", 0) + 1

    print(f"\n🔎 RESEARCHER ITERATION {iteration}")

    llm = get_llm().bind_tools(RESEARCH_TOOLS)

    system_message = SystemMessage(
        content=RESEARCH_PROMPT.format(
            question=state["question"],
            plan=state["plan"],
        )
    )

    # IMPORTANT:
    # Keep the previous research/tool history.
    history = state.get("messages", [])

    if iteration == 1:
        message = [
            system_message,
            *history,
            HumanMessage(
                content="Begin the research."
            ),
        ]
    else:
        message = [
            system_message,
            *history,
            HumanMessage(
                content=(
                    "Continue the research.\n\n"
                    "Review the evidence returned by the previous research.\n\n"
                    f"Verifier feedback:\n"
                    f"{state.get('verification', '')}\n\n"
                    "Use the verifier feedback to identify what evidence is "
                    "missing.\n"
                    "Do not repeat the same search query.\n"
                    "Perform a different, targeted search that addresses "
                    "the missing evidence.\n"
                    "If sufficient evidence is now available, stop researching."
                )
            )
        ]

    print("🤖 Calling Ollama...")

    response = llm.invoke(message)

    print("✅ Ollama responded")

    return {
        "messages": [response],
        "research_iterations": iteration,
    }