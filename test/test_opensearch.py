from researchagent.retrieval.opensearch  import get_opensearch_client


def main():

    client = get_opensearch_client()

    info = client.info()

    print("Connected to OpenSearch ✅")
    print("Cluster:", info["cluster_name"])
    print("Version:", info["version"]["number"])


if __name__ == "__main__":
    main()