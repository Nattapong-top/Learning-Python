'''
Exercise Set 9-2 : Nested While Loop (Step by Step)
==================================================
Problem 1: ReverseNumberStairWhile
โจทย์: บันไดตัวเลขแบบกลับด้าน
==================================================
คำอธิบาย:
จงเขียนฟังก์ชันชื่อ ReverseNumberStairWhile
รับจำนวนเต็ม N
แล้วแสดงตัวเลขแบบขั้นบันไดกลับด้าน
โดยบรรทัดแรกแสดงตัวเลขตั้งแต่ 1 ถึง N
บรรทัดถัดไปแสดง 1 ถึง N-1
ทำเช่นนี้ไปจนเหลือเลข 1
ต้องใช้ while ซ้อน while เท่านั้น
Test Case:
Input:
4
Expected Output:
1234
123
12
1
'''

def ReverseNumberStairWhile(n:int):
    #n = int(input('Nums: '))
    i = 1
    while i <= n:
        j = 1
        while j <= (n-i+1):
            print(j, end='')
            j += 1
        print()
        i += 1
ReverseNumberStairWhile(4)
        
'''
==================================================
Problem 2: EvenNumberTableWhile
โจทย์: ตารางเลขคู่ด้วย while
==================================================

คำอธิบาย:
จงเขียนฟังก์ชันชื่อ EvenNumberTableWhile
รับจำนวนเต็ม N
แล้วแสดงตารางตัวเลขดังนี้
แต่ละบรรทัดให้แสดงเลขคู่ เริ่มจาก 2
โดยแต่ละบรรทัดมีจำนวนตัวเลขเท่ากับลำดับบรรทัด
ต้องใช้ while ซ้อน while เท่านั้น

Test Case:
Input:
4

Expected Output:
2
2 4
2 4 6
2 4 6 8
'''
print()
def EvenNumberTableWhile(n:int):
    i = 1
    while i <= n:
        j = 2
        k = 1
        while k <= (i):
            total = j*k
            print(total, end=' ')
            k += 1
        print()
        i += 1
EvenNumberTableWhile(6)
print('-'*50)
def EvenNumberTableWhile(n:int):
    i = 1
    while i <= n:
        j = 2
        k = 1
        while k <= i:
            total = j+k
            if total % 2 == 0:
                print(total, end=' ')
            k += 1
        print()
        i += 1
EvenNumberTableWhile(4)




'''
==================================================
Problem 3: LimitedStarRowWhile
โจทย์: แถวดาวแบบจำกัดจำนวน
==================================================

คำอธิบาย:
จงเขียนฟังก์ชันชื่อ LimitedStarRowWhile
รับจำนวนเต็ม N
แสดงดาวเป็นแถว ๆ โดยแถวที่ i มีดาว i ดวง
แต่ถ้าจำนวนดาวในแถวใดมากกว่า 5
ให้หยุดแสดงดาวในแถวนั้นทันที
แล้วไปแสดงแถวถัดไป
ต้องใช้ while ซ้อน while และใช้เงื่อนไขหยุดลูปด้านใน

Test Case:
Input:
7

Expected Output:
*
**
***
****
*****
*****
*****
     

==================================================
Problem 4: CountPositiveNumbersWhile
โจทย์: นับจำนวนเลขบวกจากหลายบรรทัด
==================================================

คำอธิบาย:
จงเขียนฟังก์ชันชื่อ CountPositiveNumbersWhile
รับข้อมูลจากผู้ใช้ทีละบรรทัด
แต่ละบรรทัดมีจำนวนเต็มหลายตัวคั่นด้วยช่องว่าง
โปรแกรมหยุดเมื่อผู้ใช้พิมพ์ END
ให้นับเฉพาะจำนวนที่เป็นเลขบวก (> 0)
ต้องใช้ while ซ้อน while เท่านั้น

Test Case:
Input:
1 -2 3
0 4 -5
6
END

Expected Output:
4


==================================================
Problem 5: MultiplicationTriangleWhile
โจทย์: สามเหลี่ยมผลคูณ
==================================================

คำอธิบาย:
จงเขียนฟังก์ชันชื่อ MultiplicationTriangleWhile
รับจำนวนเต็ม N
แล้วแสดงผลคูณเป็นรูปสามเหลี่ยม
โดยบรรทัดที่ i ให้แสดงผลคูณของ i กับ 1 ถึง i
ถ้าผลคูณใดมากกว่า 30 ให้หยุดแสดงในบรรทัดนั้นทันที
ต้องใช้ while ซ้อน while เท่านั้น

Test Case:
Input:
5

Expected Output:
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
==================================================
'''
