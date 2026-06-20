import os
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

DATA_DIR = "data"

documents = []

for file in os.listdir(DATA_DIR):

    path = os.path.join(DATA_DIR, file)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    documents.append({"source": file, "content": content})

splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)

chunks = []

for doc in documents:

    texts = splitter.split_text(doc["content"])

    for text in texts:
        chunks.append({"source": doc["source"], "text": text})

print("Chunks:", len(chunks))

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

try:
    client.delete_collection("support_kb")
except:
    pass

collection = client.get_or_create_collection(name="support_kb")

for i, chunk in enumerate(chunks):

    embedding = model.encode(chunk["text"]).tolist()

    collection.add(
        ids=[str(i)],
        documents=[chunk["text"]],
        embeddings=[embedding],
        metadatas=[{"source": chunk["source"]}],
    )

print("Knowledge Base Indexed")
