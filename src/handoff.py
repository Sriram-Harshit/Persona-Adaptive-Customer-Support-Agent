import json


def generate_handoff(persona, query, retrieved_sources):

    handoff = {
        "persona": persona,
        "issue_summary": query,
        "documents_used": retrieved_sources,
        "actions_attempted": [
            "Knowledge base retrieval",
            "Automated response generation",
        ],
        "recommended_next_step": "Human review required",
    }

    return json.dumps(handoff, indent=4)
