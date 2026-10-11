from researchagent.retrieval.search import (
    bm25_search,
    semantic_search,
    hybrid_search
)




def main():

    query = "how can language models reduce hallucinations using external knowledge?"

    results = hybrid_search(
        query,
        top_k=5,
    )

    print("\n" + "=" * 80)
    print("HYBRID SEARCH")
    print("=" * 80)

    for i, result in enumerate(results):

        source = result["_source"]

        print(f"\n{i + 1}. {source['title']}")
        print("RRF Score:", result["_rrf_score"])
        print("ArXiv:", source["arxiv_id"])


if __name__ == "__main__":
    main()