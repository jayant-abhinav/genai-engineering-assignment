from problem1_rag.app.vectorstore.vector_store import ChromaStore

def test_chroma_initialization():

    store = ChromaStore()

    assert store.collection is not None
    assert store.count() >= 0