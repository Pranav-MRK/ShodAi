from researchagent.retrieval.retriever import HybridRetriever


def main():

    retriever = HybridRetriever(top_k=5)

    query = "How does retrieval augmented generation reduce hallucinations?"

    documents = retriever.invoke(query)

    print("\n" + "=" * 80)
    print("LANGCHAIN HYBRID RETRIEVER")
    print("=" * 80)

    for i, document in enumerate(documents, start=1):

        print(f"\n{i}. {document.metadata['title']}")
        print("ArXiv:", document.metadata["arxiv_id"])
        print("RRF:", document.metadata["rrf_score"])
        print("Content:", document.page_content[:250])


if __name__ == "__main__":
    main()