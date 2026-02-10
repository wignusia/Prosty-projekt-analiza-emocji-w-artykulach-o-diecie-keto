
import requests
from config import MODEL_URL, API_TOKEN

def get_sentiment(text: str):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(MODEL_URL, headers=headers, json={"inputs": text})
    response.raise_for_status()

    data = response.json()
    # Logika wyciągania najlepszego wyniku
    best_match = max(data[0], key=lambda x: x['score'])
    return best_match


def interpret_label(label: str) -> str:
    mapping = {
        '1 star': "BARDZO NEGATYWNY",
        '2 stars': "NEGATYWNY",
        '3 stars': "NEUTRALNY",
        '4 stars': "POZYTYWNY",
        '5 stars': "BARDZO POZYTYWNY"
    }
    return mapping.get(label, "NIEZNANY")