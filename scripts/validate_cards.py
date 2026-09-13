import json

with open("data/generated_cards.json", "r", encoding="utf-8") as file:
    cards = json.load(file)

print(f"Toplam kart: {len(cards)}")
print("\nKontrol sonuçları:\n")

seen_words = set()
valid_cards = 0

for card in cards:
    word = card["word"].strip().lower()
    forbidden = [item.strip().lower() for item in card["forbidden"]]

    errors = []

    if len(forbidden) != 5:
        errors.append("5 yasaklı kelime yok")

    if word in forbidden:
        errors.append("hedef kelime yasaklı kelimelerde")

    if len(forbidden) != len(set(forbidden)):
        errors.append("yasaklı kelime tekrarı var")

    if word in seen_words:
        errors.append("hedef kelime tekrar ediyor")

    seen_words.add(word)

    if errors:
        print(f"❌ {card['word']}:")
        for error in errors:
            print(f"   - {error}")
    else:
        print(f"✅ {card['word']}")
        valid_cards += 1

print(f"\nGeçerli kart: {valid_cards}/{len(cards)}")