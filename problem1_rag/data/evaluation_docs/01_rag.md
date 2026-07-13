# Retrieval-Augmented Generation (RAG)

## Introduction

Retrieval-Augmented Generation (RAG) is an AI architecture that combines information retrieval with large language models (LLMs). Instead of relying only on knowledge stored within a model's parameters, RAG retrieves relevant information from an external knowledge base and uses it as context when generating responses.

This approach significantly improves factual accuracy, reduces hallucinations, and enables language models to answer questions using up-to-date or domain-specific information.

---

## Why RAG is Needed

Traditional language models generate responses using information learned during training. They cannot easily access newly published documents or private organizational data.

Some limitations of standalone LLMs include:

- Hallucinating incorrect facts
- Limited knowledge after the training cutoff date
- Inability to access proprietary documents
- Lack of source attribution

RAG addresses these issues by grounding responses in retrieved documents.

---

## RAG Pipeline

A typical Retrieval-Augmented Generation workflow consists of the following steps:

1. User submits a question.
2. The question is converted into a vector embedding.
3. The embedding is compared against vectors stored in a vector database.
4. The most relevant document chunks are retrieved.
5. Retrieved context is combined with the user's question.
6. A prompt is constructed.
7. The LLM generates an answer using the retrieved context.
8. The system returns the answer along with document citations.

---

## Components of a RAG System

### Document Loader

Responsible for reading documents such as:

- PDF
- DOCX
- TXT
- HTML
- Markdown

The extracted text is normalized before indexing.

### Text Chunking

Large documents are split into smaller chunks to improve retrieval quality.

Chunking improves:

- Retrieval accuracy
- Embedding quality
- Context utilization

RecursiveCharacterTextSplitter is commonly used because it attempts to preserve paragraph boundaries.

### Embedding Model

Each chunk is transformed into a dense vector representation.

Common embedding models include:

- sentence-transformers/all-MiniLM-L6-v2
- BAAI/bge-small-en-v1.5
- multilingual embedding models

Embeddings capture semantic meaning rather than exact keywords.

### Vector Database

Embeddings are stored inside a vector database such as:

- ChromaDB
- FAISS
- Pinecone
- Milvus

The database performs similarity search to retrieve relevant chunks.

### Prompt Builder

The prompt builder combines:

- Retrieved context
- User question
- System instructions

This prompt is sent to the language model.

### Large Language Model

The language model generates the final response while remaining grounded in the retrieved context.

Examples include:

- Gemini
- GPT
- Claude
- Llama

---

## Advantages of RAG

- Reduces hallucinations
- Improves factual accuracy
- Supports private knowledge bases
- Allows document citations
- Works without retraining the LLM
- Easily updated by re-indexing documents

---

## Limitations

RAG also has some challenges.

Poor retrieval leads to poor answers.

Common issues include:

- Incorrect chunk size
- Weak embedding models
- Missing metadata
- Low-quality documents
- Irrelevant retrieval

Careful tuning is required for production systems.

---

## Example

Suppose a company stores its HR policy in PDF documents.

Instead of training an LLM on those documents, the PDFs are indexed into a vector database.

When an employee asks:

> "How many maternity leave days are available?"

The retriever finds the relevant HR policy section.

Only that section is provided to the LLM, which generates a grounded answer with the document citation.

---

## Best Practices

- Use semantic chunking.
- Store metadata with every chunk.
- Retrieve multiple relevant chunks.
- Keep prompts concise.
- Use citation-based responses.
- Monitor retrieval quality.
- Re-index documents after updates.

---

## Summary

Retrieval-Augmented Generation combines retrieval systems with language models to produce accurate, grounded, and explainable responses. It enables AI applications to work with dynamic and private knowledge bases while minimizing hallucinations and improving user trust.