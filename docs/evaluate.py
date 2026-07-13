import csv
import json
import time
import requests

RAG_URL = "http://127.0.0.1:8000/ask"
JUDGE_URL = "http://127.0.0.1:8001/judge"

INPUT_FILE = "docs/evaluation_dataset.json"
OUTPUT_FILE = "docs/evaluation_results.csv"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    questions = json.load(f)

results = []

for item in questions:

    question = item["question"]
    print(f"Evaluating: {question}")
    start = time.perf_counter()

    rag_response = requests.post(
        RAG_URL,
        json={"question": question},
        timeout=60,
    )

    rag_response.raise_for_status()
    latency = (time.perf_counter() - start) * 1000
    rag = rag_response.json()
    answer = rag["answer"]
    sources = ", ".join(
        source["source"]
        for source in rag.get("sources", [])
    )

    try:
        judge_response = requests.post(
            JUDGE_URL,
            json={
                "question": question,
                "answer": answer,
            },
            timeout=60,
        )

        judge_response.raise_for_status()
        judge = judge_response.json()

        overall = judge["overall_score"]
        relevance = judge["relevance"]["score"]
        correctness = judge["correctness"]["score"]
        clarity = judge["clarity"]["score"]

    except Exception as e:
        print(f"Judge failed for question {item['id']}: {e}")

        overall = None
        relevance = None
        correctness = None
        clarity = None

    results.append(
        {
            "id": item["id"],
            "question": question,
            "answer": answer,
            "sources": sources,
            "latency_ms": round(latency, 2),
            "overall_score": judge["overall_score"],
            "relevance": judge["relevance"]["score"],
            "correctness": judge["correctness"]["score"],
            "clarity": judge["clarity"]["score"],
        }
    )
    print("Waiting 10 seconds to avoid Gemini rate limit...")
    time.sleep(10)

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8",
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=results[0].keys(),
    )

    writer.writeheader()
    writer.writerows(results)

print(f"\nEvaluation completed.")
print(f"Results saved to: {OUTPUT_FILE}")

avg_overall = sum(
    r["overall_score"] for r in results
) / len(results)

avg_latency = sum(
    r["latency_ms"] for r in results
) / len(results)

print(f"\nAverage Overall Score : {avg_overall:.2f}")
print(f"Average Latency       : {avg_latency:.2f} ms")