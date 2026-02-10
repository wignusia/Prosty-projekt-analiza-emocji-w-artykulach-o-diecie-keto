import glob
import logging
from config import MAX_CHARS
from sentiment_service import get_sentiment, interpret_label

def main():
    lista_plikow = glob.glob("*.txt")

    if not lista_plikow:
        print("Nie znaleziono żadnych plików .txt w folderze!")
        return

    print(f"Znaleziono {len(lista_plikow)} plików do analizy.\n")
    print(f"{'NAZWA PLIKU':<20} | {'SENTYMENT':<20} | {'PEWNOŚĆ'}")
    print("-" * 60)

    for sciezka in lista_plikow:
        try:
            with open(sciezka, "r", encoding="utf-8") as f:
                tekst = f.read().strip()[:MAX_CHARS]

            if not tekst:
                continue

            result = get_sentiment(tekst)

            label = result['label']
            score = result['score'] * 100

            print(f"{sciezka:<20} | {interpret_label(label):<20} | {score:.2f}%")

        except Exception as e:
            logging.error(f"Błąd w pliku {sciezka}: {e}")

if __name__ == "__main__":
    main()
