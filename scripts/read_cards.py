import json

with open("data/sample_cards.json", "r", encoding="utf-8") as file:
    cards = json.load(file)

print("Total cards:", len(cards))
print("\nCard validation:")

for card in cards:
    word = card["word"].strip().lower()
    forbidden = [item.strip().lower() for item in card["forbidden"]]

    if word in forbidden:
        print(f"❌ {card['word']}: target word is in forbidden words!")
        continue

    if len(forbidden) != len(set(forbidden)):
        print(f"❌ {card['word']}: duplicate forbidden words!")
        continue

    print(f"✅ {card['word']}: valid")