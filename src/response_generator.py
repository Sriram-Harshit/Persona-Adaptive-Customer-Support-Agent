def generate_response(query, persona, retrieved_docs):

    if not retrieved_docs:
        return "No relevant information was found in the knowledge base."

    context = "\n\n".join(retrieved_docs)

    if persona == "Technical Expert":
        return f"""
Technical Support Response

Based on the available documentation:

{context}

Please review the troubleshooting steps above.
""".strip()

    if persona == "Frustrated User":
        return f"""
I understand this issue can be frustrating.

Please follow these steps:

{context}

If the issue continues, please contact support.
""".strip()

    return f"""
Business Summary

{context}

Please review the information above for operational impact and resolution guidance.
""".strip()
