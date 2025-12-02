'''แบบฝึกหัด 6-2 ข้อที่ 1
จงเขียนฟังก์ชัน to_celsius(f) ที่รับอุณหภูมิในหน่วยองศาฟาเรนไฮต์ 
เพื่อแปลงและคืนผลกลับเป็นอุณหภูมิในหน่วยองศาเซลเซียส'''

def to_celsius(f:float):
    c = (f - 32) * (5/9)
    return c

def to_fahrenheit(c:float):
    f = (c * (9/5)) + 32
    return f

# รับ str ประมวลผลว่า 25f to c and 50c to f
temp = '25'
c = to_celsius(float(temp))
print(f'{temp} Fahrenheit = {c:.2f} Celsius')

f = to_fahrenheit(float(temp))
print(f'{temp} Celsius = {f:.2f} Fahrenheit')


'''แบบฝึกหัด 6-2 ข้อที่ 2
จงเขียนฟังก์ชัน triangle_area 
รับพารามิเตอร์สามตัวแทนความยาวด้านทั้งสามของสามเหลี่ยม 
ฟังก์ชันนี้คำนวณและคืนพื้นที่ของสามเหลี่ยมเป็นผลลัพธ์ 
หมายเหตุ: สามเหลี่ยมที่มีความยาวด้านทั้งสามเป็น 
a, b และ c จะมีพื้นที่เท่ากับ √s(s−a)(s−b)(s−c) โดยที่ s=a+b+c2'''

def triangle_area(a:int, b:int, c:int) -> float:
    s = (a + b + c) / 2

    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    return area
 
a, b, c = 5, 5, 5
area = triangle_area(a, b, c)
print(f'Area: {area:,.2f}')

'''จงเขียนฟังก์ชัน is_prime รับจำนวนเต็มบวกเป็นพารามิเตอร์หนึ่งตัว 
ฟังก์ชันนี้ทดสอบและคืนผลว่าจำนวนเต็มที่รับมาเป็นจำนวนเฉพาะหรือไม่ ถ้าเป็น 
ก็คืนจริง ถ้าไม่เป็นจำนวนเฉพาะ ก็คืนเท็จ'''

def is_prime(n:int) -> bool:
    if n <= 1 : return False
    
    for k in range(2, n):
        if n % k == 0:
            return False
    return True

number = 7
check_prime = is_prime(number)
print(f'prime {number}:', check_prime)

'''แบบฝึกหัด 6-2 ข้อที่ 4
กำหนดให้มีฟังชัน is_prime(n) ซึ่งทดสอบว่า n เป็นจำนวนเฉพาะหรือไม่ ให้ใช้แล้ว จงเขียนฟังก์ชัน is_twin_prime ที่รับจำนวนเต็มบวก 2 จำนวน มาตรวจสอบว่า จำนวนเต็มทั้งสองเป็น twin primes หรือไม่ หมายเหตุ: a กับ b เป็น twin primes ก็เมื่อ a กับ b ต่างกัน 2 พอดี และทั้งคู่เป็นจำนวนเฉพาะ เช่น 3 กับ 5, 13 กับ 11 เป็นต้น'''

def is_twin_prime(a:int, b:int):
    if abs(a-b) == 2:
        return is_prime(a) and is_prime(b)

    return False

# a, b = 3, 5
a, b = 7, 10
check_twin_prime = is_twin_prime(a, b)
print(f'twin prime {a}, {b}:', check_twin_prime)

