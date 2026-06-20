# Persona-Adaptive Customer Support Agent

## Overview

Persona-Adaptive Customer Support Agent is an AI-powered customer support system that combines Retrieval-Augmented Generation (RAG), persona detection, and escalation handling to deliver personalized support responses.

The system identifies the type of user, retrieves relevant information from a knowledge base, generates context-aware responses, and escalates sensitive cases to human support when necessary.

---

## Features

- Persona Detection using Gemini
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database
- Semantic Search using Sentence Transformers
- Adaptive Responses based on user persona
- Human Escalation Workflow
- Human Handoff Summary Generation
- Streamlit User Interface

---

## Supported Personas

### Technical Expert

Provides detailed technical explanations, troubleshooting guidance, and root-cause analysis.

### Frustrated User

Uses empathetic language, simple instructions, and actionable solutions.

### Business Executive

Focuses on business impact, concise communication, and resolution guidance.

---

## System Architecture

```text
User Query
    ↓
Persona Detection
    ↓
Document Retrieval (ChromaDB)
    ↓
Escalation Check
    ↓
Adaptive Response Generation
    ↓
Human Handoff (if required)
```

---

## Project Structure

```text
persona-support-agent/
│
├── app.py
│
├── data/
│   ├── password_reset.md
│   ├── login_issues.md
│   ├── api_authentication.md
│   ├── billing_policy.md
│   ├── refund_policy.md
│   ├── account_lockout.md
│   ├── service_outage.md
│   ├── subscription_faq.md
│   ├── user_management.md
│   └── troubleshooting.md
│
├── chroma_db/
│
├── src/
│   ├── persona_detector.py
│   ├── response_generator.py
│   ├── escalation.py
│   ├── handoff.py
│   ├── rag_pipeline.py
│   ├── test_retrieval.py
│   └── main_test.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## Technologies Used

### Frontend

- Streamlit

### Backend

- Python

### Large Language Model

- Gemini 2.5 Flash

### Vector Database

- ChromaDB

### Embedding Model

- all-MiniLM-L6-v2

### Libraries

- Sentence Transformers
- LangChain Text Splitters
- Python Dotenv

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Sriram-Harshit/Persona-Adaptive-Customer-Support-Agent.git
cd Persona-Adaptive-Customer-Support-Agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Git Bash:

```bash
source venv/Scripts/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

## Build Knowledge Base

```bash
python src/rag_pipeline.py
```

Expected Output:

```text
Chunks: XX
Knowledge Base Indexed
```

---

## Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Example Queries

### Technical Expert

```text
Can you explain the API authentication failure and provide troubleshooting details?
```

### Frustrated User

```text
I've tried everything and nothing works. I cannot reset my password.
```

### Business Executive

```text
How will this outage impact operations and when will it be resolved?
```

### Escalation Scenario

```text
I want a refund for duplicate charges.
```

---
