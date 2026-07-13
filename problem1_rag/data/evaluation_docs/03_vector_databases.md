# Vector Databases

## Introduction

A vector database is a specialized database designed to store, index, and search high-dimensional vector embeddings. Unlike traditional relational databases that search using exact values or keywords, vector databases perform similarity search by comparing the semantic meaning of vectors.

Vector databases are a fundamental component of Retrieval-Augmented Generation (RAG) systems because they enable efficient retrieval of relevant document chunks based on meaning rather than exact keyword matches.

---

## Why Traditional Databases Are Not Enough

Traditional databases such as MySQL or PostgreSQL are optimized for structured data and exact lookups.

For example:

```sql
SELECT * FROM employees WHERE id = 101;
```

This query searches for an exact value.

However, semantic search requires finding information that is conceptually similar rather than identical. This is not practical using SQL alone.

---

## How Vector Databases Work

The workflow of a vector database typically consists of the following steps:

1. Documents are converted into text.
2. Text is divided into smaller chunks.
3. Each chunk is transformed into an embedding vector.
4. Embeddings are stored inside the vector database.
5. User queries are converted into embeddings.
6. Similarity search retrieves the nearest document vectors.

The retrieved chunks are then passed to a language model to generate a grounded response.

---

## Similarity Search

Instead of searching for exact keywords, vector databases compare mathematical distances between vectors.

Common similarity metrics include:

- Cosine Similarity
- Euclidean Distance
- Dot Product

Cosine similarity is the most commonly used metric for text embeddings because it measures the angle between vectors rather than their magnitude.

---

## Approximate Nearest Neighbor (ANN)

Searching millions of vectors sequentially is computationally expensive.

Vector databases use Approximate Nearest Neighbor (ANN) algorithms to retrieve highly similar vectors efficiently without comparing every stored vector.

Popular ANN algorithms include:

- HNSW (Hierarchical Navigable Small World)
- IVF (Inverted File Index)
- PQ (Product Quantization)

These methods provide a balance between search speed and retrieval accuracy.

---

## Popular Vector Databases

Several vector databases are widely used in modern AI systems.

### ChromaDB

- Open-source
- Easy Python integration
- Persistent storage
- Metadata support
- Ideal for prototypes and small-to-medium applications

### FAISS

- Developed by Meta AI
- Extremely fast
- Optimized for local similarity search
- Does not provide a built-in persistent database

### Pinecone

- Managed cloud service
- Automatic scaling
- High availability
- Suitable for enterprise applications

### Milvus

- Distributed vector database
- Supports billions of vectors
- Production-ready architecture

---

## Metadata

Besides storing embeddings, vector databases also store metadata.

Typical metadata includes:

- File name
- Document ID
- Chunk number
- Page number
- Source path

Metadata enables citation generation and document filtering during retrieval.

---

## Advantages

Using a vector database provides several benefits:

- Semantic search
- Fast retrieval
- Scalable indexing
- Metadata filtering
- Efficient storage of embeddings
- Improved RAG performance

---

## Limitations

Despite their strengths, vector databases have limitations:

- Depend on embedding quality
- Require periodic re-indexing
- Consume storage for embeddings
- Retrieval quality depends on chunking strategy

---

## Example

Suppose an organization has thousands of technical manuals.

A user asks:

> "How do I reset the administrator password?"

Instead of searching every document manually, the vector database retrieves only the most relevant chunks discussing password reset procedures.

These chunks are supplied to the language model, which generates a precise answer grounded in the retrieved documents.

---

## Summary

Vector databases enable semantic search by storing embedding vectors and performing similarity search. They are an essential component of modern Retrieval-Augmented Generation systems because they provide efficient access to relevant information while supporting metadata and scalable retrieval.