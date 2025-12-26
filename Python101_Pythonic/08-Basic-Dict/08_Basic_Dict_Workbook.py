'''บทที่ 08: Tuple, Dictionary and Set (ส่วนของ Dictionary)'''

prices = {'กาแฟ':50, 'ชาเขียว':40}

prices['โกโก้'] = 45
# prices['ชาเขียว'] = 60
print(prices)


print('นมสด' in prices) # เช็คว่ามี นมสด ใน dict ไหม
del prices['กาแฟ']      # ลบเมนูกาแฟออก
print(len(prices))      # นับจำนวน item ใน dict
print(prices)

'''บทที่ 08 (ต่อ): การดึงข้อมูลทั้งหมดออกมาดู (Traversing Dictionary)'''

#1. ดึงเฉพาะชื่อป้าย (Keys) -> .keys()
print(list(prices.keys()))

# ดึงเฉพาะ values()
print(list(prices.values()))

# 3. ดึงออกมาทั้งคู่เป็นแพ็ค (Items) -> .items()
print(list(prices.items()))

'''การวนลูป (Loop) กับ Dictionary'''
#สูตรที่ 1: วนลูปหยิบ Key (ท่ามาตรฐาน)
for menu in prices:
    print(menu)

#สูตรที่ 2: วนลูปหยิบทั้ง Key และ Value (ท่าโปร) อันนี้ป๋าต้องจำเลยครับ ได้ใช้ทำงานจริงแน่นอน
for menu, price in prices.items():
    print(menu, 'ราคา', price, 'บาท')

'''แบบฝึกหัดทดสอบ (Mini-Lab)
โจทย์: ร้านค้าของเรากำลังจะจัดโปรโมชั่น "ลดราคาทุกเมนู 5 บาท"'''

for menu, price in prices.items():
    discount = price - 5
    print(menu, 'เหลือ', discount, 'บาท')

'''การประยุกต์ใช้ Dict เพื่อนับจำนวน (Frequency Count)'''

# โจทย์: จงนับจำนวนตัวอักษรในคำว่า "mississippi"

word = 'mississippi'
letter_counts = {}

for c in word:
    if c in letter_counts:
        letter_counts[c] += 1
    else:
        letter_counts[c] = 1

print(letter_counts)

'''ตัวอย่างจากหนังสือ (หน้า 103): ระบบทะเบียนนิสิต
โจทย์: จงเขียนโปรแกรมรับข้อมูลนิสิต (รหัสนิสิต และ คณะ) 
ไปเรื่อยๆ จนกว่าจะพิมพ์ 'q' จากนั้นให้พิมพ์รายชื่อคณะที่มีนิสิตเรียนอยู่ (ไม่ซ้ำกัน)'''

# 1. สร้าง Dict เปล่าๆ ไว้เก็บข้อมูล
def students_regit():
    student_db = {}

    print('ป้อนรหัสนิสิตและคณะ (พิมพ์ q เพื่อจบ): ')

    # 2. วนลูปรับข้อมูลไปเรื่อยๆ
    while True:
        data = input()
        if data == 'q':
            break

        # 3.แยกชิ้นส่วน
        parts = data.split()
        sid = parts[0]          # รหัสนิสิต
        faculty = parts[1]      # คณะ

        # 4. เก็บลง dict
        student_db[sid] = faculty

    # 5. แสดงผล
    print('-' * 20)
    print(f'มีข้อมูลนิสิตทั้งหมด {len(student_db):,} คน')
    print('รายชื่อคณะที่มีนิสิตเรียนอยู่: ')

    # 6. ใช้ set() เพื่อกรองเอาแต่คณะที่ไม่ซ้ำกัน
    all_faculties = set(student_db.values())
    for fac in all_faculties:
        print(fac)

# students_regit()

'''เรื่องผิดบ่อย ในการใช้ dict (Common Mistakes)'''
'''❌ 1. เรียกหา Key ที่ไม่มีอยู่จริง (KeyError)
นี่คือ Error ยอดฮิตอันดับ 1 ครับ'''

scores = {'A':80, 'B':70}
# print(scores['C'])  error หา C ไม่พบ

# วิธีแก้: ใช้คำสั่ง get หรือเช็คด้วย in ก่อนเสมอ
# 1. ใช้ .get()
print(scores.get('C', 0))

# 2. ใช้ if 
if 'C' in scores:
    print(scores['C'])

# ❌ 2. เอา List มาทำเป็น Key (TypeError)
# กฎเหล็กคือ "ห้ามใช้อะไรที่แก้ค่าได้มาเป็นกุญแจ"
my_key = [1, 2]
# data = {my_key: 'Error แน่ๆ'} #TypeError: unhashable type: 'list'

# วิธีแก้: เปลี่ยน List เป็น Tuple (เพราะ Tuple แก้ค่าไม่ได้)
my_key = tuple(my_key)
data = {my_key: 'ไม่เอ๋อ'}
print(data)


# '''❌ 3. ลืมไปว่า Dict ไม่เรียงลำดับ (ใน Python รุ่นเก่า)
# แม้ Python รุ่นใหม่ๆ (3.7+) จะจำลำดับการใส่ข้อมูลได้ แต่หนังสือเรียนมักจะเตือนไว้ว่า "อย่าเชื่อใจลำดับใน Dict" ถ้าลำดับสำคัญจริงๆ ให้ใช้ List เก็บข้อมูลแทน หรือใช้ OrderedDict ครับ'''


'''การบ้าน (จาก Labbook ผสม Workbook)'''

# '''โจทย์: ให้เขียนโปรแกรม "สมุดโทรศัพท์ (Phonebook)"
# รับชื่อเพื่อนและเบอร์โทร (เว้นวรรค) ไปเรื่อยๆ จนกว่าจะพิมพ์ 'stop'
# เก็บข้อมูลลง Dict โดยให้ ชื่อเป็น Key และ เบอร์โทรเป็น Value
# หลังจากรับข้อมูลเสร็จ ให้รับชื่อเพื่อนอีก 1 ครั้ง
# ถ้ามีชื่อนี้: ให้พิมพ์เบอร์โทรออกมา
# ถ้าไม่มี: ให้พิมพ์ว่า "Not Found"'''

def phone_book():
    phonebook = {}

    while True:
        data = input('กรอกชื่อ เบอร์โทร: ').strip().split()
        if data[0] == 'stop':
            break

        name = data[0]
        number = data[1]

        phonebook[name] = number
    
    check = input('ค้นชื่อ: ').strip()
    if check in phonebook:
        print(phonebook[check])
    else:
        print('Not Found')
# phone_book()


'''8-4: Checking Key Existence'''

'''โจทย์: "เครื่องคิดเงินหน้าร้าน" 
จงเขียนฟังก์ชัน check_price(product_name) 
โดยใช้ข้อมูลราคาสินค้าจาก Dict ที่กำหนดให้
ถ้ามีสินค้า: ให้คืนค่าราคาสินค้านั้น
ถ้าไม่มีสินค้า: ให้คืนข้อความว่า "สินค้าหมด"'''

prices = {
    'mama': 6,
    'water': 10,
    'lay': 20
}

def check_price(product_name):
    return prices.get(product_name, 'สินค้าหมด')
# เทสเคส
print(check_price('mama'))   # ต้องได้ 6
print(check_price('pepsi'))  # ต้องได้ "สินค้าหมด"


