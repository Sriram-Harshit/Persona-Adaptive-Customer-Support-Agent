# Persona-Adaptive Customer Support Agent

## Overview

Persona-Adaptive Customer Support Agent is a customer support system that combines Retrieval-Augmented Generation (RAG), semantic search, persona detection, and escalation handling to deliver personalized support responses.

The system identifies the type of user, retrieves relevant information from a knowledge base, generates persona-specific responses, and escalates sensitive cases to human support when necessary.

---

## Features

- Rule-Based Persona Detection
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
Response Generation
    ↓
Escalation Check
    ↓
Human Handoff
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
└── .gitignore
```

---

## Technologies Used

### Frontend

- Streamlit

### Backend

- Python 3.11+

### Vector Database

- ChromaDB

### Embedding Model

- all-MiniLM-L6-v2

### Libraries

- Sentence Transformers
- LangChain Text Splitters
- Python Dotenv

### Response Engine

- Rule-Based Adaptive Response Generation

---

## Tech Stack

| Component              | Technology               |
| ---------------------- | ------------------------ |
| Frontend               | Streamlit                |
| Backend                | Python                   |
| Vector Database        | ChromaDB                 |
| Embeddings             | all-MiniLM-L6-v2         |
| Embedding Framework    | Sentence Transformers    |
| Chunking               | LangChain Text Splitters |
| Environment Management | Python Dotenv            |

---

## Architecture Diagram

```text
User Query
    ↓
Persona Detection
    ↓
Document Retrieval
    ↓
Response Generation
    ↓
Escalation Check
    ↓
Human Handoff
```

---

## Persona Detection Strategy

The system uses a rule-based classification approach.

### Technical Expert

Detected when the query contains technical keywords such as:

- API
- Authentication
- Token
- Endpoint
- Logs
- Error
- Configuration

### Frustrated User

Detected when the query contains emotional or frustration indicators such as:

- Nothing works
- Frustrated
- Angry
- Urgent
- Cannot
- Can't

### Business Executive

Used as the default persona when the query does not match technical or frustration indicators.

The detected persona influences the style and detail level of the generated response.

---

## RAG Pipeline Design

### Chunking Strategy

Knowledge base documents are split using RecursiveCharacterTextSplitter.

Configuration:

- Chunk Size: 400
- Chunk Overlap: 50

This improves retrieval accuracy while preserving context.

### Embedding Model

The system uses:

```text
all-MiniLM-L6-v2
```

to convert document chunks into dense vector embeddings.

### Vector Database Choice

ChromaDB was selected because it is:

- Lightweight
- Open Source
- Easy to Deploy
- Fast for Semantic Search

### Retrieval Strategy

The user query is converted into an embedding.

ChromaDB performs similarity search and returns the most relevant document chunks.

The retrieved chunks are then used to generate the final response.

---

## Escalation Logic

The system escalates sensitive requests to a human agent.

### Escalation Triggers

- Refund requests
- Billing disputes
- Payment issues
- Legal concerns
- Account deletion requests
- Missing knowledge base information

### Confidence Thresholds

The current implementation uses rule-based escalation rather than numerical confidence scores.

Escalation occurs whenever predefined sensitive keywords are detected or no relevant documents are retrieved.

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

No environment variables are required.

The application runs completely locally without external API dependencies.

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

Can you explain the API authentication failure and provide troubleshooting details?

### Frustrated User

I've tried everything and nothing works. I cannot reset my password.

### Business Executive

How will this outage impact operations and when will it be resolved?

### Login Issue

I am unable to log into my account after several attempts.

### Subscription Question

Can I upgrade my subscription plan immediately?

### Escalation Scenario

I want a refund for duplicate charges.

---

## Known Limitations

- Persona detection is rule-based and may not capture complex user intent.
- No multi-turn conversation memory.
- Limited to the information available in the knowledge base.
- Human handoff is simulated and not connected to a real ticketing system.
- Responses are generated from retrieved knowledge base content only.

---

## Future Improvements

- LLM-based persona classification
- Multi-turn conversation memory
- Real ticketing system integration
- User authentication
- Analytics dashboard
- Additional customer personas
- Confidence-based escalation scoring

---

## Repository

GitHub: https://github.com/Sriram-Harshit/Persona-Adaptive-Customer-Support-Agent

---

## Author

Sri Ram Harshit
