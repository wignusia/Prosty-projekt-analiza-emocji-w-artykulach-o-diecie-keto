
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HF_TOKEN")

if not API_TOKEN:
    raise RuntimeError("Brak HF_TOKEN w pliku .env")


MODEL_URL = "https://router.huggingface.co/hf-inference/models/nlptown/bert-base-multilingual-uncased-sentiment"
MAX_CHARS = 1000