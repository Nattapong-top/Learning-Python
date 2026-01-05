'''
Nested List as Matrix (บท 9 ต่อ)
1) Matrix คืออะไร (ในมุม Python)

Matrix = list ซ้อน list
'''

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

'''
โครงสร้าง:

m → ทั้งตาราง

m[i] → แถวที่ i

m[i][j] → คอลัมน์ j ในแถว i

2) ความสัมพันธ์กับ nested loop (ของเดิมที่ป๋าเพิ่งเรียน)
'''

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end=' ')
    print()

'''
📌 Rule สำคัญ

outer loop = แถว

inner loop = คอลัมน์

index ตัวหน้า = row, ตัวหลัง = column

3) การเข้าถึงข้อมูล Matrix (ต้องแม่น)'''

print(m[0])
print(m[0][1])
print(m[2][2])

'''ถ้าเขียนตำแหน่งพลาด'''

#print(m[1][3])  # IndexError: list index out of range

'''เพราะ index เริ่มที่ 0 และคอลัมน์มีแค่ 0–2
4) สร้าง Matrix ด้วย loop (หัวใจบทนี้)
4.1 สร้าง matrix เปล่า'''

matrix = []

for i in range(3):
    row = []
    for j in range(4):
        row.append(0)
    matrix.append(row)

print(matrix)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=' ')
    print()
'''
0 0 0 0
0 0 0 0
0 0 0 0'''



for row in range(len(matrix)):
    print(matrix[row])

'''
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]'''

'''📌 จุดที่เด็กพลาดบ่อย

row = []
matrix.append(row)
ต้องอยู่ “ใน loop แถว” เสมอ ไม่งั้นทุกแถวจะชี้ list เดียวกัน'''

'''5) Pattern ความคิดแบบจุฬาฯ (จำสูตรนี้ไว้)
Matrix Loop Template
for i in range(rows):
    for j in range(cols):
        # ทำงานกับ matrix[i][j]
        # '''


'''🧠 วิธีคิด Logic (ตามสูตร 5 ข้อที่ป๋าใช้)
ตัวอย่างโจทย์:

รับ matrix ของตัวเลข
หาผลรวมของทุกสมาชิก
1) Input
nested list (matrix)
2) Output
ผลรวม (int / float)
3) Logic (exclusive ไหม)
ทุกช่องต้องถูกนับ → nested loop
4) Edge cases
matrix ว่าง
แถวไม่เท่ากัน
5) ลำดับการเช็ก
loop แถว → loop คอลัมน์ → บวกค่า
(ยังไม่เขียนโค้ด ตามกติกาป๋า 👍)'''

'''version อ่านยาก ใช้ index โดยไม่จำเป็น'''
def matrix_sum_idx(raw_list:list)-> int:
    
    total = 0
    if not raw_list:
        return 0
    line = len(raw_list)
    for row in range(line):
        idx = len(raw_list[row])
        for col in range(idx):
            num = raw_list[row][col]
            if isinstance(num, int):
                total += num
    return total
n_list = [['t',2,24,45,67],[345,456,26,8],[34,5677,34],[-3,-345,-4564]]
print(matrix_sum_idx(n_list))


'''version อ่านง่าย ใช้ value loop'''

def matrix_sum_val(raw_list:list):
    total = 0
    if not raw_list:
        return 0
    
    for row in raw_list:
        for col in row:
            if isinstance(col,int):
                total += col
    return total
print(matrix_sum_val(n_list))

'''6) แบบฝึกหัด (ยังไม่เฉลย)
Exercise 9.2 — CountEven
นับจำนวนเลขคู่ใน matrix

🧠 วิธีคิด Logic (ตามสูตร 5 ข้อที่ป๋าใช้)

Exercise 9.2 — CountEven
นับจำนวนเลขคู่ใน matrix

1) Input
nested list (matrix)
2) Output
จำนวนนับเลขคู่ (int / float)
3) Logic (exclusive ไหม)
ทุกช่องต้องถูกนับ → nested loop
4) Edge cases
matrix ว่าง
แถวไม่เท่ากัน มีแค่เลขคี่
5) ลำดับการเช็ก
loop แถว → loop คอลัมน์ → นับเลขคู่
'''
def matrix_count_even(n_list):
    count = 0
    if not n_list:
        return 0

    for row in n_list:
        for col in row:
            if isinstance(col, int) and col % 2 == 0:
                    count += 1
    return count
print(matrix_count_even(n_list))


'''version pythonic'''
def matrix_count_even_pythonic(n_list:list):
    return sum(
        1
        for row in n_list
        for col in row
        if isinstance(col, int) and col % 2 == 0
    )

print(matrix_count_even_pythonic(n_list))


'''Exercise 9.3 — MaxInMatrix
หาค่ามากที่สุดใน matrix
(ห้ามใช้ max() กับ matrix ตรง ๆ)
1) Input
nested list (matrix)
2) Output
ค่ามากสุด (int / float)
3) Logic (exclusive ไหม)
ทุกช่องต้องถูกนับ → nested loop
4) Edge cases
matrix ว่าง
แถวไม่เท่ากัน 
5) ลำดับการเช็ก
loop แถว → loop คอลัมน์ → เก็บค่าสูงสุด
'''
def max_matrix(n_list:list):
    max_num = None
    if not n_list:
        return 0
    
    for row in n_list:
        for col in row:
            if isinstance(col, int):
                if max_num is None or max_num < col:
                    max_num = col
    return max_num

print(max_matrix(n_list))

'''version pythonic'''
def max_matrix_pythonic(n_list:list):
    values = [
        col
        for row in n_list
        for col in row
        if isinstance(col, int)
    ]
    return max(values) if values else 0
print(max_matrix_pythonic(n_list))

'''
Exercise 9.4 — RowSum
คืน list ที่เก็บผลรวมของแต่ละแถว
จุดนี้สำคัญมาก
ถ้า Nested List + Nested Loop แน่น
1) Input
- nested list (matrix)
2) Output
- list ผลรวมของแต่ละแถว (int)
3) Logic (exclusive ไหม)
- ทุกช่องต้องถูกนับ → nested loop
4) Edge cases
- matrix ว่าง แถวไม่เท่ากัน not int
5) ลำดับการเช็ก
loop แถว → loop คอลัมน์ → สะสมค่าแต่ละแถว -> เก็บใน new list
'''
def row_sum(n_list:list):
    total_list = []

    if not n_list:
        return 0
    for row in n_list:
        sum_row = 0
        for col in row:
            if isinstance(col, int):
                sum_row += col
        total_list.append(sum_row)
    return total_list
print(row_sum(n_list))

'''version pythonic'''
def row_sum_pythonic(n_list:list):
    return [
        sum(col for col in row if isinstance(col, int))
        for row in n_list
    ]
print(row_sum(n_list))

'''
บทถัดไปจะไปได้หมด:

ตารางคะแนน

ภาพ (pixel)

Grid / Board / Game

ข้อมูลเชิงโครงสร้างจริง'''