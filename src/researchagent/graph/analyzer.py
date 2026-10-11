from langchain_core.messages import HumanMessage

from researchagent.rag.llm import get_llm

ANALYZER_PROMPT = """
You are the research analyzer for Shod.

Analyze the research evidence provided below.

User question:
{question}

Research evidence:
{evidence}

Research plan:
{plan}

Your job:

1. Identify the important findings.
2. Identify evidence that directly answers the question.
3. Identify disagreements or limitations.
4. Do not invent information.
5. Only use the provided evidence.

Return a concise research analysis.
"""


def analyzer(state):
    print("\n🧠 ANALYZER STARTED")

    llm = get_llm()

    sources = state.get("sources", [])

    evidence_parts = []

    for source in sources:

        evidence_parts.append(
            f"""
            SOURCE {source.get("source_id")}

            Title: {source.get("title")}
            ArXiv: {source.get("arxiv_id")}
            URL: {source.get("url")}

            Evidence:
            {source.get("evidence")}
            """
        )

    evidence = "\n\n".join(evidence_parts)

    response = llm.invoke(
        [
            HumanMessage(
                content=ANALYZER_PROMPT.format(
                    question=state["question"],
                    evidence=evidence,
                    plan=state["plan"],
                )
            )
        ]
    )
    print("✅ ANALYZER FINISHED")


    return {
        "findings": response.content
    }