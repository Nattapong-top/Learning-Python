'''ข้อที่ 1: ทักทาย (Parameter)
โจทย์: จงสร้างฟังก์ชันชื่อ greet(name) 
หน้าที่: รับชื่อเข้ามา แล้ว Print คำว่า "Hello, [ชื่อ]"
ตัวอย่าง: greet("Paa") -> แสดงผล Hello, Paa'''

def greet(name):
    # เขียนโค้ดในนี้ (บรรทัดเดียว)
    print('Hello', name)

# ทดสอบเรียกใช้
print('--- ข้อ 1 ---')
greet("Paa") 
greet("Nat")
print('\n')


'''ข้อที่ 2: พื้นที่วงกลม (Return)
โจทย์: จงสร้างฟังก์ชันชื่อ circle_area(radius)
หน้าที่: รับรัศมี (radius) เข้ามา คำนวณพื้นที่ (3.14 * r * r) 
แล้ว **Return** ค่าพื้นที่กลับไป (ห้าม Print ในฟังก์ชัน)'''

def circle_area(radius):
    # เขียนโค้ดคำนวณ
    area = 3.14 * radius * radius
    return area

# ทดสอบเรียกใช้ (สังเกตว่าเราต้องเอา print ไปรับค่าที่ return กลับมา)
print('--- ข้อ 2 ---')
my_area = circle_area(5) 
print(f"พื้นที่รัศมี 5 คือ: {my_area}")
print(f"พื้นที่รัศมี 10 คือ: {circle_area(10)}")
print('\n')


'''ข้อที่ 3: ตัดเกรด (Return Logic)
โจทย์: จงสร้างฟังก์ชันชื่อ get_grade(score)
หน้าที่: รับคะแนนเข้ามา แล้ว Return เกรดกลับไป
- >= 80 ได้ 'A'
- >= 50 ได้ 'P'
- ต่ำกว่า 50 ได้ 'F'
'''

def get_grade(score):
    # เขียน Logic if-else
    if score >= 80 :
        return 'A'
    elif score >= 50:
        return 'P'
    else:
        return 'F'

# ทดสอบเรียกใช้
print('--- ข้อ 3 ---')
s1 = get_grade(85)
s2 = get_grade(40)
print(f"คะแนน 85 ได้เกรด: {s1}")
print(f"คะแนน 40 ได้เกรด: {s2}")
print(f"คะแนน 55 ได้เกรด:", get_grade(55))
