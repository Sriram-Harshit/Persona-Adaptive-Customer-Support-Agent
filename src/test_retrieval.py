import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("support_kb")

query = input("Query: ")

query_embedding = model.encode(query).tolist()

results = collection.query(query_embeddings=[query_embedding], n_results=3)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(results["documents"][0]):
    print(f"Result {i + 1}")
    print(doc)
    print("-" * 50)
