from researchagent.retrieval.opensearch import get_opensearch_client

INDEX_NAME = "research_papers"

INDEX_MAPPING ={
    "settings":{
        "index":{
            "knn":True
        }
    },
    "mappings":{
        "properties":{
            "title": {
                "type": "text"
            },
            "content": {
                "type": "text"
            },
            "arxiv_id": {
                "type": "keyword"
            },
            "authors": {
                "type": "keyword"
            },
            "url": {
                "type": "keyword"
            },
            "published": {
                "type": "date"
            },
            "categories": {
                "type": "keyword"
            },
            "embedding":{
                "type":"knn_vector",
                "dimension":384,
                "method":{
                    "name": "hnsw",
                    "engine": "lucene",
                    "space_type": "cosinesimil"
                }
            }
        }
    }
}


def create_index():

    client = get_opensearch_client()

    if client.indices.exists(index=INDEX_NAME):
        print(f"Index '{INDEX_NAME}' already exists.")
        return

    client.indices.create(
        index=INDEX_NAME,
        body=INDEX_MAPPING
    )

    print(f"Created index: {INDEX_NAME}")


if __name__ == "__main__":
    create_index()