import arxiv
from langchain_core.documents import Document


def search_arxiv(query:str,max_result:int=5)-> list[Document]:
    client = arxiv.Client()

    search = arxiv.Search(
        query=query,
        max_results=max_result,
        sort_by= arxiv.SortCriterion.Relevance
    )

    documents =[]

    for result in client.results(search):
        document = Document(
            page_content=result.summary,
            metadata={
                 "title": result.title,
                "authors": [author.name for author in result.authors],
                "arxiv_id": result.entry_id,
                "url": result.pdf_url,
                "published": result.published.isoformat(),
                "categories": result.categories,
            },
        )

        documents.append(document)

    return documents

