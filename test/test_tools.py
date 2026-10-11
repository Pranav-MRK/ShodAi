from researchagent.tools.research_tools import (
    arxiv_search,
    research_search,
    get_paper,
)


def main():

    print("\n" + "=" * 80)
    print("ARXIV TOOL")
    print("=" * 80)

    result = arxiv_search.invoke({
        "query": "retrieval augmented generation",
        "max_results": 2,
    })

    print(result[:3000])


    print("\n" + "=" * 80)
    print("RESEARCH SEARCH TOOL")
    print("=" * 80)

    result = research_search.invoke({
        "query": "how can RAG reduce hallucinations?",
        "top_k": 3,
    })

    print(result[:3000])


    print("\n" + "=" * 80)
    print("GET PAPER TOOL")
    print("=" * 80)

    result = get_paper.invoke({
        "arxiv_id": "2506.06962v3",
    })

    print(result[:3000])


if __name__ == "__main__":
    main()