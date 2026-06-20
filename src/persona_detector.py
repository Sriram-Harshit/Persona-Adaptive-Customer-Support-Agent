def detect_persona(message):

    text = message.lower()

    technical_keywords = [
        "api",
        "authentication",
        "endpoint",
        "token",
        "error",
        "logs",
        "configuration",
        "server",
    ]

    frustrated_keywords = [
        "frustrated",
        "angry",
        "nothing works",
        "terrible",
        "urgent",
        "annoying",
        "cannot",
        "can't",
    ]

    if any(word in text for word in technical_keywords):
        return {
            "persona": "Technical Expert",
            "confidence": "High",
            "reasoning": "Technical terminology detected.",
        }

    if any(word in text for word in frustrated_keywords):
        return {
            "persona": "Frustrated User",
            "confidence": "High",
            "reasoning": "Emotional language detected.",
        }

    return {
        "persona": "Business Executive",
        "confidence": "Medium",
        "reasoning": "General business-oriented query.",
    }
