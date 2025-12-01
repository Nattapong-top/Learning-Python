'''ข้อที่ 1: ตรวจจำนวนเฉพาะ (The Missing Piece)
โจทย์: จงเขียนฟังก์ชัน is_prime(n) เพื่อใช้คู่กับโค้ดอาจารย์
- รับตัวเลข n
- ถ้า n <= 1 ให้ return False (1 ไม่ใช่จำนวนเฉพาะ)
- ถ้ามีเลขอะไรหาร n ลงตัว (นอกจาก 1 กับตัวมันเอง) ให้ return False
- ถ้าไม่มีอะไรหารลงตัวเลย ให้ return True'''

def is_prime(n):
    # 1. ดักตัวเลขที่น้อยกว่าหรือเท่ากับ 1
    if n <= 1:
        return False
    
    # 2. วนลูปเช็คตัวหาร (ตั้งแต่ 2 ถึง n-1)
    for k in range(2, n):
        if n % k == 0:
            return False  # เจอตัวหารลงตัว! ไม่ใช่ prime แน่นอน
            
    # 3. ถ้าหลุดลูปมาได้ แปลว่าไม่มีใครหารลงตัวเลย
    return True

# --- โค้ดอาจารย์ (ตอนนี้จะ Run ได้แล้ว!) ---
def is_twin_prime(p1, p2):
    return abs(p1-p2)==2 and is_prime(p1) and is_prime(p2)

print(f"3, 5 Twin Prime? : {is_twin_prime(3, 5)}") # ต้องได้ True
print(f"10, 12 Twin Prime? : {is_twin_prime(10, 12)}") # ต้องได้ False


'''ข้อที่ 2: ตรวจสระภาษาอังกฤษ (Is Vowel?)
โจทย์: เขียนฟังก์ชัน is_vowel(c)
- รับตัวอักษร c มา 1 ตัว
- ถ้าเป็น a, e, i, o, u (ตัวเล็กหรือใหญ่ก็ได้) ให้ return True
- ถ้าไม่ใช่ ให้ return False'''

def is_vowel(c:str):
    # Hint: ใช้คำสั่ง in ช่วยได้ครับ เช่น if c.lower() in '...':
    
    # return แบบธรรมดา
    # return True if c.lower() in 'aeiou' else False
    
    # return แบบ เซียน
    return c.lower() in 'aeiou'


print(f"A is vowel? : {is_vowel('A')}")
print(f"z is vowel? : {is_vowel('z')}")


'''ข้อที่ 3: ตรวจเบอร์มือถือ (Validation)
โจทย์: เขียนฟังก์ชัน check_mobile(number)
- รับเบอร์โทรเข้ามาเป็น String
- ต้องยาว 10 ตัวอักษร (len == 10)
- ต้องขึ้นต้นด้วย '0' (startswith)
- ต้องเป็นตัวเลขทั้งหมด (isdigit)
- ถ้าครบทุกข้อ return True, ถ้าขาดแม้แต่ข้อเดียว return False'''

def check_mobile(number:str):
    # Hint: ใช้ and เชื่อม 3 เงื่อนไขเข้าด้วยกันแล้ว return ทีเดียวได้เลย
    # return ... and ... and ...
    
    # return แบบธรรมดา 
    return True if len(number) == 10    \
            and number.startswith('0')  \
            and number.isdigit() else False

    # return แบบ เซียน
    # return len(number) == 10 and number.startswith('0') and number.isdigit()


print(f"0812345678 OK? : {check_mobile('0812345678')}")
print(f"1234567890 OK? : {check_mobile('1234567890')}") # ไม่ขึ้นต้นด้วย 0