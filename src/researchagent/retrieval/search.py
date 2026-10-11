from researchagent.retrieval.opensearch import get_opensearch_client
from researchagent.retrieval.index import INDEX_NAME
from researchagent.ingestion.embeddings import get_embeddings_model


def bm25_search(
    query: str,
    top_k: int = 5,
):

    client = get_opensearch_client()

    response = client.search(
        index=INDEX_NAME,
        body={
            "size": top_k,
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": [
                        "title^2",
                        "content",
                    ],
                }
            },
        },
    )

    return response["hits"]["hits"]





def semantic_search(
    query: str,
    top_k: int = 5,
):

    client = get_opensearch_client()
    embeddings = get_embeddings_model()

    query_vector = embeddings.embed_query(query)

    response = client.search(
        index=INDEX_NAME,
        body={
            "size": top_k,
            "query": {
                "knn": {
                    "embedding": {
                        "vector": query_vector,
                        "k": top_k,
                    }
                }
            },
        },
    )

    return response["hits"]["hits"]


def reciprocal_rank_fusion(
    result_lists: list[list[dict]],
    top_k: int = 5,
    k: int = 60,
):

    scores = {}
    documents = {}

    for results in result_lists:

        for rank, result in enumerate(results, start=1):

            doc_id = result["_id"]

            score = 1 / (k + rank)

            scores[doc_id] = (
                scores.get(doc_id, 0) + score
            )

            documents[doc_id] = result

    ranked_documents = sorted(
        documents.values(),
        key=lambda result: scores[result["_id"]],
        reverse=True,
    )

    for result in ranked_documents:
        result["_rrf_score"] = scores[result["_id"]]

    return ranked_documents[:top_k]



def hybrid_search(
    query: str,
    top_k: int = 5,
):

    bm25_results = bm25_search(
        query,
        top_k=top_k,
    )

    semantic_results = semantic_search(
        query,
        top_k=top_k,
    )

    results = reciprocal_rank_fusion(
        [
            bm25_results,
            semantic_results,
        ],
        top_k=top_k,
    )

    return results