from langchain_core.documents import Document

def results_to_documents(results: list[dict]) -> list[Document]:
    documents=[]

    for result in results:
        source = result["_source"]

        documents.append(
            Document(
                page_content=source["content"],
                metadata={
                    "title": source["title"],
                    "arxiv_id": source["arxiv_id"],
                    "url": source["url"],
                    "authors": source["authors"],
                    "published": source["published"],
                    "categories": source["categories"],
                    "rrf_score": result.get("_rrf_score"),
                },
            )

        )
    return documents

