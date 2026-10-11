from researchagent.ingestion.arxiv import search_arxiv


def main():
    papers = search_arxiv(
        "retrieval augmented generation",
        max_result=3,
    )

    print(f"\nFound {len(papers)} papers\n")

    for paper in papers:
        print("=" * 80)
        print("TITLE:", paper.metadata["title"])
        print("ARXIV:", paper.metadata["arxiv_id"])
        print("URL:", paper.metadata["url"])
        print("\nABSTRACT:")
        print(paper.page_content[:500])
        print()


if __name__ == "__main__":
    main()