import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
Türkçe Tabu oyunu için 100 adet kart oluştur.

Her kart:
- 1 hedef kelime
- 5 yasaklı kelime
- 1 kategori

içersin.

Kurallar:
- Günlük hayatta kullanılan yaygın Türkçe kelimeler seç.
- Hedef kelime yasaklı kelimeler arasında olmasın.
- Yasaklı kelimeler kendi içinde tekrar etmesin.
- Her kartta tam olarak 5 yasaklı kelime olsun.
- Aynı hedef kelime birden fazla kullanılmasın.
- JSON dışında hiçbir açıklama yazma.

Format:
[
  {
    "id": 1,
    "word": "KAHVE",
    "forbidden": ["Fincan", "Kafein", "İçecek", "Türk", "Sabah"],
    "category": "Yiyecek"
  }
]
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

text = response.text.strip()

cards = json.loads(text)

with open("data/generated_cards.json", "w", encoding="utf-8") as file:
    json.dump(cards, file, ensure_ascii=False, indent=2)

print(f"{len(cards)} kart oluşturuldu.")