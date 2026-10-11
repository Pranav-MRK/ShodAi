from researchagent.ingestion.arxiv import search_arxiv
from researchagent.ingestion.chunker import split_documents

def main():
    documents = search_arxiv(
        "retrieval augmented generation",
        max_result=2,
    )
    chunks = split_documents(documents)

    print(f"\nDocuments: {len(documents)}")
    print(f"Chunks: {len(chunks)}\n")

    for i, chunk in enumerate(chunks[:5]):

        print("=" * 80)
        print("CHUNK:", i + 1)
        print("TITLE:", chunk.metadata["title"])
        print("ARXIV:", chunk.metadata["arxiv_id"])
        print("SIZE:", len(chunk.page_content))

        print("\nCONTENT:")
        print(chunk.page_content[:300])


if __name__ == "__main__":
    main()
