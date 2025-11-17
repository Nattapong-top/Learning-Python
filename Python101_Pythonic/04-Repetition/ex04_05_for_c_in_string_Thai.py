import re 

text = "ชื่อ:ณัฐพงศ์ เงินเดือน:๒๙,๐๐๐฿"
print(f"กำลังตรวจสอบ: '{text}'")

# --- นี่คือแม่แบบใหม่ที่ถูกต้อง ---
# เราระบุทุกช่วงเอง โดย "เว้น" ฿ (U+0E3F) ไว้
#
# ก-ฮ (Consonants)
# ๐-๙ (Thai Digits)
# \u0E30-\u0E3A (Vowels/Signs 1: ะ, ั, า ... ฺ)
# \u0E40-\u0E4E (Vowels/Signs 2: เ, แ, โ ... ์)
#
allowed_pattern = re.compile(
    r'[a-zA-Z0-9\s' +       # Eng, Digits, Space
    r'ก-ฮ' +                 # Thai Consonants
    r'๐-๙' +                 # Thai Digits
    r'\u0E30-\u0E3A' +       # Thai Vowels (ที่อยู่ก่อน ฿)
    r'\u0E40-\u0E4E' +       # Thai Vowels (ที่อยู่หลัง ฿)
    r']'
)
# ---------------------------------

for c in text:
    # เงื่อนไขเดิม: ถ้าไม่เจอใน "แม่แบบ"
    if not allowed_pattern.match(c):
        print(f"เจออักษรพิเศษ: '{c}'")