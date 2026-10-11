from researchagent.rag.chain import build_rag_chain


def main():

    chain = build_rag_chain()

    question = """
    What are the main approaches used to improve
    retrieval augmented generation systems?
    """

    answer = chain.invoke(question)

    print("\n" + "=" * 80)
    print("RESEARCH ANSWER")
    print("=" * 80)

    print(answer)


if __name__ == "__main__":
    main()