from typing import Any

from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever

from researchagent.retrieval.search import hybrid_search


class HybridRetriever(BaseRetriever):
    """
    LangChain retriever backed by our
    OpenSearch BM25 + semantic + RRF search.
    """

    top_k: int = 5

    def _get_relevant_documents(
        self,
        query: str,
        *,
        run_manager: CallbackManagerForRetrieverRun,
    ) -> list[Document]:

        results = hybrid_search(
            query=query,
            top_k=self.top_k,
        )

        documents = []

        for result in results:

            source = result["_source"]

            document = Document(
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

            documents.append(document)

        return documents