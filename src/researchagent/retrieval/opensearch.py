from opensearchpy import OpenSearch


def get_opensearch_client() -> OpenSearch:

    client = OpenSearch(
        hosts=[
            {
                "host": "localhost",
                "port": 9200,
            }
        ],
        use_ssl=False,
        verify_certs=False,
    )

    return client