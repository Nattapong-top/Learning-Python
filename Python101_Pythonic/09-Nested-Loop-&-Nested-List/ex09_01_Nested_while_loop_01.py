'''
Exercise Set 9-1 : Basic Nested While Loop

==================================================
Problem 1: MultiplicationTableWhile
โจทย์: ตารางสูตรคูณด้วย while
==================================================

คำอธิบาย:
จงเขียนฟังก์ชันชื่อ MultiplicationTableWhile
รับจำนวนเต็ม N จากผู้ใช้
เพื่อแสดงตารางสูตรคูณของแม่ 2 จนถึงแม่ N
โดยแสดงผลการคูณด้วย 1 ถึง 5 เท่านั้น
กำหนดให้แสดงผลแต่ละจำนวนกว้าง 4 ช่อง และจัดชิดขวา
ให้ใช้คำสั่ง while เท่านั้น (ห้ามใช้ for)

Test Case:
Input:
6

Expected Output:
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
   6  12  18  24  30
'''

def show_str(n:int):
    return f'{n:>4}'

def Multi_While(N:int):
    i = 2
    while i <= N:
        total_str = ''
        j = 1
        while  j <= 5:
            total = i*j
            total_str += show_str(total)
            j += 1
        print(total_str)
        i += 1
Multi_While(6)
# print(multi)
                


'''
==================================================
Problem 2: NumberStairWhile
โจทย์: บันไดตัวเลขด้วย while
==================================================

คำอธิบาย:
จงเขียนฟังก์ชันชื่อ NumberStairWhile
รับจำนวนเต็ม N
แล้วแสดงตัวเลขเรียงเป็นขั้นบันได
โดยบรรทัดที่ i ให้แสดงตัวเลขตั้งแต่ 1 ถึง i
ต้องใช้ while ซ้อน while เท่านั้น
Test Case:
Input:
4
Expected Output:
1
12
123
1234'''

def number_stair_while(N:int):
    i = 1
    while i <= N:
        j = 1
        while j <= i:
            print(j, end=' ')
            j += 1
        print()
        i += 1
number_stair_while(9)

'''
==================================================
Problem 3: StarStairWhile
โจทย์: บันไดดาวด้วย while
==================================================

คำอธิบาย:
จงเขียนฟังก์ชันชื่อ StarStairWhile
รับจำนวนเต็ม N
แล้วแสดงรูปดาวเป็นขั้นบันไดจำนวน N แถว
ห้ามใช้การคูณสตริง ('*' * i)
ต้องใช้ while ซ้อน while เท่านั้น
Test Case:
Input:
3
Expected Output:
*
**
***
'''
def StarStairWhile(N:int):
    i = 1
    while i <= N:
        j = 1
        while j <= i:
            print('*', end='')
            j += 1
        print()
        i += 1
StarStairWhile(9)

'''
==================================================
Problem 4: CountNumbersMultiLineWhile
โจทย์: นับจำนวนตัวเลขจากหลายบรรทัด
==================================================
คำอธิบาย:
จงเขียนฟังก์ชันชื่อ CountNumbersMultiLineWhile
รับข้อมูลจากผู้ใช้ทีละบรรทัด
ในแต่ละบรรทัดจะมีตัวเลขหลายตัวคั่นด้วยช่องว่าง
โปรแกรมจะหยุดรับข้อมูลเมื่อผู้ใช้พิมพ์คำว่า END
ให้แสดงผลว่ามีตัวเลขทั้งหมดกี่ตัว
ต้องใช้ while ซ้อน while
Test Case:
Input:
1 2 3
4 5
6
END
Expected Output:
6'''
def countNumbersMultiLineWhile():
    count = 0
    while True:
        line = input('nums: ').strip()
        if not line:
            continue
        elif line.upper() == 'END':
            break
        else:
            nums = line.split()
            j = 0
            while  j < len(nums):
                count += 1
                j += 1
    return count
# print(countNumbersMultiLineWhile())

'''
==================================================
Problem 5: LimitedMultiplicationWhile
โจทย์: ตารางสูตรคูณแบบจำกัดค่า
==================================================

คำอธิบาย:
จงเขียนฟังก์ชันชื่อ LimitedMultiplicationWhile
รับจำนวนเต็ม N
เพื่อแสดงตารางสูตรคูณของแม่ 2 ถึงแม่ N
เริ่มคูณจาก 1 เพิ่มขึ้นเรื่อย ๆ
ถ้าผลคูณของแม่ใดมีค่ามากกว่า 20
ให้หยุดแสดงผลของแม่สูตรคูณนั้นทันที
แล้วไปทำแม่ถัดไป
ต้องใช้ while ซ้อน while เท่านั้น
Test Case:
Input:
5
Expected Output:
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20
========================='''

def LimitedMultiWhile(N:int):
    i = 2
    while i <= N:
        j = 1
        while j <= N:
            total = i*j
            if total > 20:
                break
            j += 1
            print(total, end=' ')
        i += 1
        print()
LimitedMultiWhile(5)



