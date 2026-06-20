import json
import os

import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer

from src.persona_detector import detect_persona
from src.response_generator import generate_response
from src.escalation import should_escalate
from src.handoff import generate_handoff

if not os.path.exists("chroma_db"):
    try:
        import src.rag_pipeline
    except Exception as e:
        st.error(f"Failed to build knowledge base: {e}")


@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


@st.cache_resource
def load_collection():
    client = chromadb.PersistentClient(path="./chroma_db")
    return client.get_collection("support_kb")


model = load_model()
collection = load_collection()


def retrieve_documents(query, top_k=3):
    query_embedding = model.encode(query).tolist()

    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)

    docs = results["documents"][0]

    sources = []

    if results["metadatas"]:
        sources = [meta["source"] for meta in results["metadatas"][0]]

    return docs, sources


st.set_page_config(
    page_title="Persona-Adaptive Customer Support Agent", page_icon="🤖", layout="wide"
)

st.title("🤖 Persona-Adaptive Customer Support Agent")

with st.sidebar:
    st.header("System Information")
    st.write("Persona Detection: Rule-Based")
    st.write("Vector Database: ChromaDB")
    st.write("Embedding Model: all-MiniLM-L6-v2")

query = st.text_area(
    "Customer Message", height=150, placeholder="Describe your issue..."
)

if st.button("Submit"):

    if not query.strip():
        st.warning("Please enter a message.")
        st.stop()

    try:

        persona_data = detect_persona(query)
        persona = persona_data["persona"]

        docs, sources = retrieve_documents(query)

        escalate = should_escalate(query, docs)

        if escalate:

            handoff = generate_handoff(persona, query, sources)

            st.subheader("Response")
            st.error("Your request requires review by a human support representative.")

            with st.expander("Human Handoff Summary"):
                st.json(json.loads(handoff))

        else:

            response = generate_response(query, persona, docs)

            st.subheader("Response")
            st.write(response)

    except Exception as e:
        st.error(str(e))
