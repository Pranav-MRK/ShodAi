from langchain_core.prompts import ChatPromptTemplate


RESEARCH_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI research assistant.

Answer the user's research question using ONLY
the provided research context.

Rules:

1. Do not invent facts.
2. If the context is insufficient, say so.
3. Cite claims using the provided paper metadata.
4. Distinguish evidence from your own synthesis.
5. Prefer precise technical explanations.
6. Mention conflicting evidence when present.

Research context:

{context}
""",
        ),
        (
            "human",
            "{question}",
        ),
    ]
)