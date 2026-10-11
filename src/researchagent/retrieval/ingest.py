from researchagent.retrieval.opensearch import get_opensearch_client
from researchagent.retrieval.index import INDEX_NAME
from researchagent.ingestion.arxiv import search_arxiv
from researchagent.ingestion.embeddings import get_embeddings_model
from researchagent.ingestion.chunker import split_documents


def ingest_documents(query:str,max_result:int = 5):
    print(f"Searching ArXiv for:{query}")

    documents = search_arxiv(
        query=query,
        max_result=max_result
    )

    print(f"Found {len(documents)} papers")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    embeddings = get_embeddings_model()
    client = get_opensearch_client()

    for i,chunk in enumerate(chunks):
        vector = embeddings.embed_query(
            chunk.page_content
        )

        document ={
            "title":chunk.metadata["title"],
            "content":chunk.page_content,
            "arxiv_id": chunk.metadata["arxiv_id"],
            "authors": chunk.metadata["authors"],
            "url": chunk.metadata["url"],
            "published": chunk.metadata["published"],
            "categories": chunk.metadata["categories"],
            "embedding": vector,
        }

        client.index(
            index=INDEX_NAME,
            body=document,
        )

        print(f"Indexed chunk {i + 1}/{len(chunks)}")
        client.indices.refresh(index=INDEX_NAME)

    print("\nIngestion completed ✅")


if __name__ == "__main__":

    ingest_documents(
        query="retrieval augmented generation",
        max_result=5,
    )

