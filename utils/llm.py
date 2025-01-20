import os
import requests

# Set up environment variables or constants for your Groq API key
GROQ_API_KEY = "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"
GROQ_ENDPOINT = "https://api.groq.com/query"  # Replace with the actual Groq endpoint

def query_groq(prompt):  # Renamed from parse_with_groq to query_groq
    """
    Sends a query to Groq and returns the result.
    """
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "query": prompt,
    }

    response = requests.post(GROQ_ENDPOINT, headers=headers, json=data)

    # Handle response from Groq
    if response.status_code == 200:
        result = response.json()
        return result.get("response", "")
    else:
        print("Error with Groq API:", response.status_code, response.text)
        return ""
