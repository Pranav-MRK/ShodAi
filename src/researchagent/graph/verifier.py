from langchain_core.messages import HumanMessage
from researchagent.rag.llm import get_llm


VERIFIER_PROMPT = """
You are the evidence verifier for Shod.

Check whether the research analysis is properly supported
by the provided research evidence.

User question:
{question}

Research findings:
{findings}

Research evidence:
{sources}

Check:

1. Are the important findings supported by the evidence?
2. Are there unsupported claims?
3. Are there contradictions?
4. Is the evidence sufficient to answer the question?

Return:

VERDICT: PASS or NEEDS_MORE_RESEARCH

REASON:
A short explanation.
"""


def verifier(state):
    print("\n🔍 VERIFIER STARTED")

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
                content=VERIFIER_PROMPT.format(
                    question=state["question"],
                    findings=state.get("findings", ""),
                    sources=evidence,
                )
            )
        ]
    )

    verification = response.content

    if "VERDICT: NEEDS_MORE_RESEARCH" in verification:
        decision = "NEEDS_MORE_RESEARCH"
    elif "VERDICT: PASS" in verification:
        decision = "PASS"
    else:
        decision = "NEEDS_MORE_RESEARCH"

    print(f"🔍 Verification decision: {decision}")
    print("✅ VERIFIER FINISHED")

    return {
        "verification": verification,
        "verification_decision": decision,
    }