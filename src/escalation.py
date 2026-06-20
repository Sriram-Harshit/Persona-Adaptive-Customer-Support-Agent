def should_escalate(query, retrieved_docs):

    sensitive_keywords = [
        "refund",
        "billing",
        "payment",
        "charge",
        "legal",
        "lawsuit",
        "account deletion",
    ]

    query_lower = query.lower()

    if any(word in query_lower for word in sensitive_keywords):
        return True

    if not retrieved_docs:
        return True

    return False
