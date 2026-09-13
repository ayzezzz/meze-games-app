import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

FILE_PATH = "data/generated_cards.json"
NEW_CARD_COUNT = 100

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        existing_cards = json.load(file)
else:
    existing_cards = []

existing_words = {
    card["word"].strip().lower()
    for card in existing_cards
}

prompt = f"""
Generate {NEW_CARD_COUNT} NEW cards for a Turkish Taboo game.

Each card must contain:
- 1 target word
- 5 forbidden words
- 1 category

Rules:
- All target words, forbidden words, and categories must be in Turkish.
- Use common Turkish words that are frequently used in everyday life.
- Do not reuse any target word from the existing dataset.
- The target word must not appear among its forbidden words.
- Each card must contain exactly 5 forbidden words.
- Forbidden words must be unique within each card.
- Return valid JSON only. Do not include any explanation or Markdown.

Existing target words:
{sorted(existing_words)}

Format:
[
  {{
    "id": 1,
    "word": "KAHVE",
    "forbidden": ["Fincan", "Kafein", "İçecek", "Sıcak", "Sabah"],
    "category": "Yiyecek & İçecek"
  }}
]
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

new_cards = json.loads(response.text.strip())

next_id = len(existing_cards) + 1

for card in new_cards:
    card["id"] = next_id
    next_id += 1

all_cards = existing_cards + new_cards

with open(FILE_PATH, "w", encoding="utf-8") as file:
    json.dump(all_cards, file, ensure_ascii=False, indent=2)

print(f"Existing cards: {len(existing_cards)}")
print(f"New cards added: {len(new_cards)}")
print(f"Total cards: {len(all_cards)}")