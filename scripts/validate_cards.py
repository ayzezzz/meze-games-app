import json

with open("data/generated_cards.json", "r", encoding="utf-8") as file:
    cards = json.load(file)

print(f"Total cards: {len(cards)}")
print("\nValidation results:\n")

seen_words = set()
valid_cards = 0

for card in cards:
    word = card["word"].strip().lower()
    forbidden = [item.strip().lower() for item in card["forbidden"]]

    errors = []

    if len(forbidden) != 5:
        errors.append("not exactly 5 forbidden words")

    if word in forbidden:
        errors.append("target word appears in forbidden words")

    if len(forbidden) != len(set(forbidden)):
        errors.append("duplicate forbidden words")

    if word in seen_words:
        errors.append("duplicate target word")

    seen_words.add(word)

    if errors:
        print(f"❌ {card['word']}:")
        for error in errors:
            print(f"   - {error}")
    else:
        print(f"✅ {card['word']}")
        valid_cards += 1

print(f"\nValid cards: {valid_cards}/{len(cards)}")