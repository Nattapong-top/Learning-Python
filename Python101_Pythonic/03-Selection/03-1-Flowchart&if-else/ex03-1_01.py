'''
รับข้อมูล
int a, int b
a < b True
min = a
max = b
else
min = b
max = a
print(min, max)
'''
# แบบธรรมดา
def if_01():
    a = 10 #input()
    b = 5  #input()

    if a < b:
        min = a
        max = b
    else:
        min = b
        max = a
    print(f' ตัวแปรน้อยที่สุด: {min}, ตัวแปรมากสุด: {max}')
# if_01()

# แบบ pythonic
def if_01_01():
    a = 20
    b = 19

    # 1. สมมติขึ้นมาเลยว่า a < b เพื่อกำหนดตัวแปร
    min_val, max_val = a, b

    # 2. ตรวจสอบ สมมุติ ว่าเป็นจริงไหม ตัว if
    if a > b:
        # 3. ถ้า ค่าตัวแปรที่เราสมมติผิด ก็ให้ลับตัวแปร
        min_val, max_val = b, a

    print(f'ค่าน้อยสุด:{min_val}, ค่ามากสุด:{max_val}')
# if_01_01()

# pythonic อีกวิธี
def if_01_02():
    a, b, c, d = 20, 40, 44, 43

    # ใช้ function min(), max()
    min_val = min(a, b, c, d)
    max_val = max(a, b, c, d)

    print(f'ค่าน้อยสุด:{min_val}, ค่ามากสุด:{max_val}')
# if_01_02()


def if_02():
    a = 10
    b = 9

    # abs() คือฟังก์ชันหาค่าสัมบูรณ์ คือค่าจะเป็นบวกเสมอ
    if abs(a - b) > 2:
        a, b = b, a
    
    else:
        a = b**2 + a
    
    print(a, b)
# if_02()

def if_03(a:int):
        
    if a%2 == 0:  # a เป็นจำนวนคู่ ?
        a *= 2
    elif a > 10:
        a //= 2
    else:
        a = 0
    return a
# print(if_03(19))


def if_04(a:int, b:int = 0):
    if a % 2 == 0:
        b = 2 * a
        
        if a > 10:
            a //= 2
        
        else:
            b += a

        a += b
    a *= 2

    return a, b
# print('8, 4', if_04(8, 4))
# print('11, 41', if_04(111, 41))
# print('3, 1', if_04(3, 1))

def if_05(month: int):
    # เชียนแบบธรรมดา
    # if month == 4 or month == 6 or month == 9 \
        # or month == 11:
    # เขียนแบบ pythonic
    if month in [4, 6, 9, 11]:
        return f'เดือนที่ {month}: ลงท้ายด้วย "ยน"'
    elif not month == 2:
        return f'เดือนที่ {month}: ลงท้ายด้วย "คม"'
    else:
        return f'เดือนที่ {month}: ลงท้ายด้วย "พันธ์"'
        
def calling_if_05():
    print(if_05(1))
    print(if_05(2))
    print(if_05(4))
    print(if_05(9))
    print(if_05(3))
# calling_if_05()

