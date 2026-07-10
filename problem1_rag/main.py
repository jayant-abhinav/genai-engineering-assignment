from problem1_rag.app.vectorstore.vector_store import ChromaStore


def main():

    store = ChromaStore()

    print("Stored vectors:", store.count())


if __name__ == "__main__":
    main()