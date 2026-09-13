import json

with open("data/sample_cards.json", "r", encoding="utf-8") as file:
    cards = json.load(file)

print("Toplam kart:", len(cards))
print("\nKart kontrolleri:")

for card in cards:
    word = card["word"].strip().lower()
    forbidden = [item.strip().lower() for item in card["forbidden"]]

    if word in forbidden:
        print(f"❌ {card['word']}: hedef kelime yasaklı kelimelerde!")
        continue

    if len(forbidden) != len(set(forbidden)):
        print(f"❌ {card['word']}: yasaklı kelimelerde tekrar var!")
        continue

    print(f"✅ {card['word']}: uygun")