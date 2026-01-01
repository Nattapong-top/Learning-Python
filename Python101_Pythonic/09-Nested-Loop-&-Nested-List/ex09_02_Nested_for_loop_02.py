'''
==================================================
ex09_02_Nested_for_loop_02
ชุดโจทย์ฝึก Nested for loop (10 ข้อ)
==================================================

=====================
[BASIC LEVEL]
=====================

1) Problem Name (EN): PrintSquareStars
   ชื่อโจทย์ (TH): พิมพ์สี่เหลี่ยมดาว

   Description:
   รับเลข n
   พิมพ์สี่เหลี่ยมดาวขนาด n x n
   ใช้ nested for loop

   Logic (วิธีคิด):
   1) Input: n
   2) Output: ดาว n แถว แถวละ n ตัว
   3) Loop ซ้อนหรือไม่: ใช่ (แถว x คอลัมน์)
   4) Edge cases: n = 1
   5) ลำดับการเช็ก: วนแถวก่อน แล้ววนคอลัมน์

   Function Name:
   print_square_stars(n)

   Test Case:
   Input: 3
   Output:
   ***
   ***
   ***
'''
# --------------------------------
def print_square_stars(n:int):
    for i in range(n):
        for j in range(n):
            print('*', end='')
        print()
print_square_stars(3)

'''
2) Problem Name (EN): PrintNumberTable
   ชื่อโจทย์ (TH): ตารางตัวเลขคูณตำแหน่ง

   Description:
   รับเลข n
   พิมพ์ตาราง n x n
   ช่องแถว i คอลัมน์ j แสดงค่า i*j

   Logic:
   1) Input: n
   2) Output: ตารางตัวเลข
   3) Loop ซ้อนหรือไม่: ใช่
   4) Edge cases: n = 1
   5) ลำดับการเช็ก: คำนวณ i*j ทุกช่อง

   Function Name:
   print_number_table(n)

   Test Case:
   Input: 3
   Output:
   1 2 3
   2 4 6
   3 6 9
'''
# --------------------------------
def print_number_table(n:int):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i*j, end=' ')
        print()
print_number_table(3)

'''
3) Problem Name (EN): PrintLeftAlignedStarTriangle
   ชื่อโจทย์ (TH): พิมพ์สามเหลี่ยมดาวชิดซ้าย

   Description:
   รับเลข n
   พิมพ์สามเหลี่ยมดาวชิดซ้าย สูง n

   Logic:
   1) Input: n
   2) Output: แถวที่ i มีดาว i ตัว
   3) Loop ซ้อนหรือไม่: ใช่
   4) Edge cases: n = 0
   5) ลำดับการเช็ก: แถวเพิ่ม → ดาวเพิ่ม

   Function Name:
   print_left_aligned_star_triangle(n)

   Test Case:
   Input: 4
   Output:
   *
   **
   ***
   ****
'''
# --------------------------------
def print_left_aligned_star_triangle(n:int):
    for row in range(1, n+1):
        for _ in range(row):
            print('*', end='')
        print()
print_left_aligned_star_triangle(5)

'''
4) Problem Name (EN): PrintDescendingNumbers
   ชื่อโจทย์ (TH): พิมพ์ตัวเลขลดหลั่น

   Description:
   รับเลข n
   แถวแรกพิมพ์ n ถึง 1
   แถวถัดไปลดลงทีละ 1

   Logic:
   1) Input: n
   2) Output: รูปสามเหลี่ยมตัวเลข
   3) Loop ซ้อนหรือไม่: ใช่
   4) Edge cases: n = 1
   5) ลำดับการเช็ก: จำนวนตัวเลขลดตามแถว

   Function Name:
   print_descending_numbers(n)

   Test Case:
   Input: 4
   Output:
   4321
   321
   21
   1
'''
# --------------------------------
def print_descending_numbers(n:int):
    for line in range(n, 0, -1):
        for num in range(line, 0, -1):
            print(num, end='')
        print()
print_descending_numbers(5)

'''
5) Problem Name (EN): CountAllPairs
   ชื่อโจทย์ (TH): นับจำนวนคู่ตัวเลข

   Description:
   รับเลข n
   นับจำนวนคู่ (i, j) ที่ i < j

   Logic:
   1) Input: n
   2) Output: จำนวนคู่
   3) Loop ซ้อนหรือไม่: ใช่
   4) Edge cases: n < 2
   5) ลำดับการเช็ก: i ก่อน j=i+1

   Function Name:
   count_all_pairs(n)

   Test Case:
   Input: 4
   Output: 6
'''
# --------------------------------
def count_all_pairs(n:int):
    count = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if i < j:
                count += 1
    return count
print(count_all_pairs(4))



# =====================
# [UP LEVEL]
# =====================

'''
6) Problem Name (EN): PrintRightAlignedStarTriangle
   ชื่อโจทย์ (TH): พิมพ์สามเหลี่ยมดาวชิดขวา

   Description:
   รับเลข n
   พิมพ์สามเหลี่ยมดาวชิดขวา

   Logic:
   1) Input: n
   2) Output: สามเหลี่ยมดาวชิดขวา
   3) Loop ซ้อนหรือไม่: ใช่
   4) Edge cases: n = 1
   5) ลำดับการเช็ก: ช่องว่างก่อน → ดาว

   Function Name:
   print_right_aligned_star_triangle(n)

   Test Case:
   Input: 4
   Output:
      *
     **
    ***
   ****
'''
# --------------------------------


'''
7) Problem Name (EN): PrintStarPyramid
   ชื่อโจทย์ (TH): พิมพ์พีระมิดดาว

   Description:
   รับเลข n
   พิมพ์พีระมิดสูง n

   Logic:
   1) Input: n
   2) Output: พีระมิดดาว
   3) Loop ซ้อนหรือไม่: ใช่
   4) Edge cases: n = 1
   5) ลำดับการเช็ก: ช่องว่าง → ดาว (2*i-1)

   Function Name:
   print_star_pyramid(n)

   Test Case:
   Input: 3
   Output:
     *
    ***
   *****
'''
# --------------------------------


'''
8) Problem Name (EN): PrintMultiplicationTriangle
   ชื่อโจทย์ (TH): สามเหลี่ยมสูตรคูณ

   Description:
   แถวที่ i พิมพ์ i*j เมื่อ j ≤ i

   Logic:
   1) Input: n
   2) Output: สามเหลี่ยมตัวเลข
   3) Loop ซ้อนหรือไม่: ใช่
   4) Edge cases: n = 1
   5) ลำดับการเช็ก: คูณตามตำแหน่ง

   Function Name:
   print_multiplication_triangle(n)

   Test Case:
   Input: 4
   Output:
   1
   2 4
   3 6 9
   4 8 12 16
'''
# --------------------------------


'''
9) Problem Name (EN): PrintHollowSquare
   ชื่อโจทย์ (TH): พิมพ์สี่เหลี่ยมโปร่ง

   Description:
   พิมพ์ขอบเป็นดาว ด้านในเป็นช่องว่าง

   Logic:
   1) Input: n
   2) Output: ตารางดาว
   3) Loop ซ้อนหรือไม่: ใช่
   4) Edge cases: n ≤ 2
   5) ลำดับการเช็ก: ขอบก่อน กลางทีหลัง

   Function Name:
   print_hollow_square(n)

   Test Case:
   Input: 5
   Output:
   *****
   *   *
   *   *
   *   *
   *****
'''
# --------------------------------


'''
10) Problem Name (EN): FindClosestPair1toN
    ชื่อโจทย์ (TH): หาคู่ตัวเลขที่ต่างกันน้อยที่สุด

    Description:
    รับเลข n
    พิจารณาคู่ (i, j) เมื่อ i < j
    หาค่า |i - j| ที่น้อยที่สุด

    Logic:
    1) Input: n
    2) Output: ค่าผลต่างน้อยสุด
    3) Loop ซ้อนหรือไม่: ใช่
    4) Edge cases: n < 2
    5) ลำดับการเช็ก: เทียบทุกคู่

    Function Name:
    find_closest_pair_1_to_n(n)

    Test Case:
    Input: 5
    Output: 1
'''
# --------------------------------
