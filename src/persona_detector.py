import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def detect_persona(message):

    prompt = f"""
Classify the customer message into exactly one persona.

Personas:
1. Technical Expert
2. Frustrated User
3. Business Executive

Return ONLY valid JSON:

{{
    "persona": "",
    "confidence": "",
    "reasoning": ""
}}

Message:
{message}
"""

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    text = response.text.strip()
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)
