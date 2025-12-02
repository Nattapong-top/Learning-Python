'''ข้อที่ 1: ปริมาตรทรงกระบอก (Geometry)
1. Helper Function:ชื่อฟังก์ชัน: get_circle_area(radius)
ตัวแปรรับเข้า: radius (float)
หน้าที่: คำนวณและคืนค่าพื้นที่วงกลม (pi r^2) (กำหนดให้ pi = 3.14)'''

def get_circle_area(radius:float):

    pi = 3.14
    a = pi * (radius ** 2)

    return a

'''2. Main Function:
ชื่อฟังก์ชัน: get_cylinder_volume(radius, height)
ตัวแปรรับเข้า: radius (float), height (float)
หน้าที่: คำนวณปริมาตรทรงกระบอก โดยต้อง เรียกใช้ get_circle_area มาช่วยคำนวณ แล้วคืนค่าปริมาตรกลับไป'''

def get_cylinder_volume(radius:float, height:float):

    pi_r = get_circle_area(radius)
    v = pi_r * height
    return v

area = get_cylinder_volume(4, 1)
print(area)


'''ข้อที่ 2: ราคารวมภาษี (Finance)
1. Helper Function:
ชื่อฟังก์ชัน: calculate_vat(price)
ตัวแปรรับเข้า: price (float)
หน้าที่: คำนวณและคืนค่าภาษี 7% ของราคา (ราคา * 0.07)
'''
def calculate_vat(price:float):
    total_vat = price * 0.07
    return total_vat


'''
2. Main Function:
ชื่อฟังก์ชัน: get_net_price(price)
ตัวแปรรับเข้า: price (float)
หน้าที่: คืนค่าราคาสุทธิ (ราคาต้น + ภาษี) โดยต้อง เรียกใช้ calculate_vat มาหาค่าภาษีก่อน'''
def get_net_price(price:float):

    total_vat = calculate_vat(price)
    total_price = price + total_vat
    return total_price

sale = 100000
total_price = get_net_price(sale)
print(total_price)

'''ข้อที่ 3: กรองเลขติดลบ (List Logic)
1. Helper Function:
ชื่อฟังก์ชัน: is_positive(n)
ตัวแปรรับเข้า: n (int)
หน้าที่: คืนค่า True ถ้า n มากกว่าหรือเท่ากับ 0, คืนค่า False ถ้า n ติดลบ
'''
def is_positive(n:int):
    return True if n >= 0 else False

'''
2. Main Function:
ชื่อฟังก์ชัน: filter_positive(numbers)
ตัวแปรรับเข้า: numbers (list ของ int)
หน้าที่: สร้าง List ใหม่ที่เก็บเฉพาะเลขที่เป็นบวกจาก numbers โดยการวนลูปและ เรียกใช้ is_positive เพื่อตรวจสอบเงื่อนไข แล้วคืนค่า List ใหม่ออกมา'''

def filter_positive(numbers:list):
    return [n for n in numbers if is_positive(n)]


numbers = [-1, -2, -3, -4, -5, 0, 1]

positive_number = filter_positive(numbers)
print(positive_number)


'''ข้อที่ 4: ตรวจสอบปีอธิกสุรทิน (Leap Year Logic)
1. Helper Function:
ชื่อฟังก์ชัน: is_leap_year(year)
ตัวแปรรับเข้า: year (int)
หน้าที่: คืนค่า True ถ้าหารด้วย 4 ลงตัว (คิดแบบง่ายๆ ไม่ต้องสนเงื่อนไข 100/400 ปี), ถ้าไม่ลงตัวคืนค่า False
'''
def is_leap_year(year:int):
    return True if year % 4 == 0 else False


'''
2. Main Function:
ชื่อฟังก์ชัน: days_in_feb(year)
ตัวแปรรับเข้า: year (int)
หน้าที่: คืนค่าจำนวนวันในเดือนกุมภาพันธ์ ของปีนั้นๆ โดย เรียกใช้ is_leap_year
ถ้าเป็น Leap Year ให้คืนค่า 29
ถ้าไม่เป็น ให้คืนค่า 28'''

def day_in_feb(year:int):
    if is_leap_year(year):
        return 29
    else:
        return 28

year = 2000
chack_day = day_in_feb(year)
print(chack_day)

'''
ข้อที่ 5: งานทางฟิสิกส์ (Physics)
1. Helper Function:
ชื่อฟังก์ชัน: calculate_force(mass, accel)
ตัวแปรรับเข้า: mass (float), accel (float)
หน้าที่: คำนวณแรง (F = ma) และคืนค่าผลลัพธ์
'''
def calculate_force(mass:float, accel:float):
    f = mass * accel
    return f

'''2. Main Function:
ชื่อฟังก์ชัน: calculate_work(mass, accel, distance)
ตัวแปรรับเข้า: mass (float), accel (float), distance (float)
หน้าที่: คำนวณงาน (W = F x d) โดยต้อง เรียกใช้ calculate_force 
เพื่อหาแรงก่อน แล้วค่อยเอาไปคูณระยะทาง คืนค่าผลลัพธ์'''

def calculate_work(mass:float, accel:float, distance:float):
    f = calculate_force(mass, accel)
    w = f * distance
    return w

mass, accel, distance = 10, 2, 3
work = calculate_work(mass, accel, distance)
print(work)
