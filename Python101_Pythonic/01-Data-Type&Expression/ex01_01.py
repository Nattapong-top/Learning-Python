# รับเลขจำนวนเต็ม 2 จำนวนที่คั่นด้วยช่องว่าง แล้วแสดงผลบวกของเลขทั้งสอง
# 2 3 = 5
'''
เขียนแบบวิธีทั่วไป 
# 1. รับค่า input มาเป็น string 1 บรรทัด
input_line = input()

# 2. แยก string นั้นด้วยช่องว่าง จะได้เป็น list ของ string
# เช่น "2 3" จะกลายเป็น ['2', '3']
parts = input_line.split()

# 3. แปลงค่าใน list จาก string เป็น integer
a = int(parts[0])  # a = 2
b = int(parts[1])  # b = 3

# 4. นำมาบวกกันแล้วพิมพ์ผลลัพธ์
print(a + b)

'''

# แบบ pythonic
a, b = map(int, input().split())

print(a + b)
