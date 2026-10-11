from langchain_core.tools import tool
import json
from researchagent.ingestion.arxiv import search_arxiv
from researchagent.retrieval.opensearch import get_opensearch_client
from researchagent.retrieval.index import INDEX_NAME
from researchagent.retrieval.retriever import HybridRetriever


@tool
def arxiv_search(query:str,max_result:int=5) ->str:
    """
    Search ArXiv for research papers related to a query.

    Use this when the user needs to discover recent or
    potentially relevant research papers.
    """

    documents = search_arxiv(
        query =query,
        max_result=max_result
    )
    if not documents:
        return "No documents found."

    results=[]

    for document in documents:
        metadata = document.metadata

        results.append(
            f"""
            Title: {metadata["title"]}
            Authors: {", ".join(metadata["authors"])}
            ArXiv: {metadata["arxiv_id"]}
            URL: {metadata["url"]}
            Published: {metadata["published"]}

            Abstract:
            {document.page_content}

            """
        )
    return "\n---\n".join(results)
    

@tool
def research_search(query: str, top_k: int = 5) -> str:
    """
    Search the research knowledge base using hybrid BM25
    and semantic retrieval with Reciprocal Rank Fusion.

    Use this when answering a research question requires
    evidence from the indexed research corpus.
    """

    retriever = HybridRetriever(
        top_k=top_k
    )

    documents = retriever.invoke(query)

    if not documents:
        return json.dumps({
            "query": query,
            "sources": []
        })

    sources = []

    for i, document in enumerate(documents, start=1):

        metadata = document.metadata

        sources.append({
            "source_id": i,
            "title": metadata.get("title", ""),
            "arxiv_id": metadata.get("arxiv_id", ""),
            "url": metadata.get("url", ""),
            "evidence": document.page_content,
        })

    return json.dumps({
        "query": query,
        "sources": sources
    })


@tool
def get_paper(arxiv_id: str) -> str:
    """
    Retrieve indexed chunks belonging to a specific ArXiv paper.

    Use this when the agent needs to inspect a particular paper
    in more detail.
    """

    client = get_opensearch_client()

    paper_id = arxiv_id.strip()

    if not paper_id.startswith("http"):
        paper_id = f"http://arxiv.org/abs/{paper_id}"

    response = client.search(
        index=INDEX_NAME,
        body={
            "size": 20,
            "query": {
                "term": {
                    "arxiv_id": paper_id
                }
            }
        },
    )

    hits = response["hits"]["hits"]

    if not hits:
        return f"No indexed content found for {arxiv_id}."

    # Keep chunks in their OpenSearch order for now.
    # We'll improve chunk metadata later.
    results = []

    for i, hit in enumerate(hits, start=1):

        source = hit["_source"]

        results.append(
            f"""
CHUNK {i}

Title: {source["title"]}
ArXiv: {source["arxiv_id"]}
URL: {source["url"]}

Content:
{source["content"]}
"""
        )

    return "\n---\n".join(results)

