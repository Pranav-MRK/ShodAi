from researchagent.retrieval.search import hybrid_search
from researchagent.rag.llm import get_llm
from researchagent.rag.prompts import RESEARCH_PROMPT
from researchagent.retrieval.retriever import HybridRetriever


from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough




def format_documents(documents):

    context_parts = []

    for i, document in enumerate(documents, start=1):

        metadata = document.metadata

        context_parts.append(
            f"""
            SOURCE {i}

            Title: {metadata["title"]}
            ArXiv: {metadata["arxiv_id"]}
            URL: {metadata["url"]}

            Content:
            {document.page_content}
            """
        )

    return "\n".join(context_parts)


def build_rag_chain():

    retriever = HybridRetriever(
        top_k=5
    )

    llm = get_llm()

    chain = (
        {
            "context": retriever | format_documents,
            "question": RunnablePassthrough(),
        }
        | RESEARCH_PROMPT | llm | StrOutputParser()
    )

    return chain