import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_response(query, persona, retrieved_docs):

    context = "\n\n".join(retrieved_docs)

    styles = {
        "Technical Expert": """
You are a senior technical support engineer.

Provide:
- Technical explanations
- Root cause analysis
- Troubleshooting steps

Use only the supplied context.
""",
        "Frustrated User": """
You are an empathetic support specialist.

Provide:
- Understanding and reassurance
- Clear action steps
- Simple explanations

Use only the supplied context.
""",
        "Business Executive": """
You are a business support representative.

Provide:
- Concise answers
- Business impact
- Resolution guidance

Use only the supplied context.
""",
    }

    prompt = f"""
{styles.get(persona, styles["Business Executive"])}

CONTEXT:
{context}

QUESTION:
{query}

Rules:
- Answer only from the context.
- Do not invent information.
- If information is unavailable, clearly say so.
"""

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    return response.text
