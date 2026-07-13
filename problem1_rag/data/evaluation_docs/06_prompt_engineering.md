# Prompt Engineering

## Introduction

Prompt Engineering is the process of designing and refining prompts to guide a Large Language Model toward producing accurate, useful, and structured responses.

Rather than modifying the model itself, prompt engineering controls model behavior through carefully designed instructions and context.

It is one of the most important techniques for improving the performance of Retrieval-Augmented Generation systems.

---

## Why Prompt Engineering Matters

Large Language Models are highly capable, but their outputs depend heavily on how instructions are written.

A well-designed prompt can:

- Improve factual accuracy
- Reduce hallucinations
- Produce consistent output
- Enforce formatting requirements
- Improve reasoning quality

Poor prompts often lead to vague or incorrect responses.

---

## Prompt Structure

A typical prompt consists of several components:

### System Instructions

These define the model's role.

Example:

```
You are an AI assistant that answers questions using only the provided context.
```

---

### Context

Retrieved document chunks are inserted into the prompt.

Example:

```
Context:
...
```

This grounds the model's response in factual information.

---

### User Question

The user's query is appended after the retrieved context.

Example:

```
Question:
What is semantic search?
```

---

### Response Instructions

The prompt may specify:

- Response length
- Tone
- Formatting
- Citation requirements
- Restrictions

Example:

```
If the answer cannot be found in the provided context, say so clearly.
```

---

## Prompting Techniques

### Zero-Shot Prompting

The model receives only instructions.

Example:

```
Explain vector databases.
```

---

### Few-Shot Prompting

Examples are included before the user's query.

This helps the model learn the expected response format.

---

### Chain-of-Thought Prompting

The model is encouraged to reason step by step before producing a final answer.

This technique often improves performance on reasoning tasks.

---

## Prompt Engineering in RAG

Retrieval-Augmented Generation combines retrieved context with prompt engineering.

A PromptBuilder typically assembles:

- System instructions
- Retrieved document chunks
- User question
- Output guidelines

The completed prompt is then sent to the language model.

---

## Reducing Hallucinations

Prompt engineering helps reduce hallucinations by instructing the model to:

- Answer only using retrieved context.
- Avoid unsupported claims.
- Indicate when information is unavailable.
- Cite document sources.

These instructions increase user trust and improve factual accuracy.

---

## Output Formatting

Prompts can require structured output.

Examples include:

- JSON
- Markdown
- Bullet points
- Tables

Structured output is especially useful for APIs and automated systems.

---

## Best Practices

- Keep prompts concise.
- Provide sufficient context.
- Use explicit instructions.
- Avoid ambiguity.
- Specify the desired output format.
- Test and refine prompts iteratively.

---

## Example Prompt

```
You are an AI assistant.

Use only the provided context to answer the user's question.

If the answer is not present in the context, clearly state that the information is unavailable.

Context:
...

Question:
What is ChromaDB?
```

---

## Summary

Prompt engineering is a fundamental technique for controlling Large Language Models. By combining clear instructions with retrieved context, RAG systems can generate accurate, grounded, and consistent responses while minimizing hallucinations.