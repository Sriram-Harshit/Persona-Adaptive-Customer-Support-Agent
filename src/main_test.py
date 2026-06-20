from persona_detector import detect_persona
from response_generator import generate_response
from escalation import should_escalate
from handoff import generate_handoff

import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("support_kb")


def retrieve_documents(query, top_k=3):

    query_embedding = model.encode(query).tolist()

    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)

    docs = results["documents"][0]

    sources = []

    if results["metadatas"]:
        sources = [meta["source"] for meta in results["metadatas"][0]]

    return docs, sources


def main():

    print("\n=== Persona-Adaptive Customer Support Agent ===\n")

    query = input("Ask: ")

    persona_data = detect_persona(query)

    persona = persona_data["persona"]

    print("\nDetected Persona:")
    print(persona)

    print("\nConfidence:")
    print(persona_data["confidence"])

    docs, sources = retrieve_documents(query)

    print("\nRetrieved Sources:")

    for source in sources:
        print("-", source)

    escalate = should_escalate(query, docs)

    print("\nEscalation Status:")
    print(escalate)

    if escalate:

        handoff = generate_handoff(persona, query, sources)

        print("\n=== HUMAN HANDOFF SUMMARY ===")
        print(handoff)

    else:

        response = generate_response(query, persona, docs)

        print("\n=== GENERATED RESPONSE ===")
        print(response)


if __name__ == "__main__":
    main()
