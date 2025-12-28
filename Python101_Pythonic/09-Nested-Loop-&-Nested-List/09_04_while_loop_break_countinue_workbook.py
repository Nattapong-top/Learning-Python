'''
📘 บทฝึก: break / continue
'''

'''
🧾 ข้อ 1
รับตัวเลขไปเรื่อย ๆ
ถ้าเจอ 0 ให้หยุด
แล้วคืนผลรวมของเลขทั้งหมดก่อนหน้า
'''

def sum_until_zero():
    total = 0
    while True:
        n = int(input('num: '))
        if n == 0:
            break
        total += n
    return total
# print(sum_until_zero())

'''
🧾 ข้อ 2
รับ list ของตัวเลข
ให้รวมเฉพาะเลขคู่ (ใช้ continue)
'''

def sum_even(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] % 2 != 0:
            i += 1
            continue
        total += nums[i]
        i += 1

    return total
print(sum_even([1, 2, 3, 4, 5, 6]))


'''
📘 บทฝึก: Nested while loop
'''

'''
🧾 ข้อ 1
จงพิมพ์ตารางสูตรคูณ 1 ถึง n
ใช้ nested while
'''

def mult_table(n):
    i = 1
    result = []
    while i <= n:
        j = 1
        while j <= n:
            result.append(f"{i}*{j} = {i*j}")
            j += 1
        i += 1
    return result
print(mult_table(3))

# mult_table(3)


'''
🧾 ข้อ 2
จงพิมพ์รูปแบบดังนี้ (n แถว)

*
**
***
****

ใช้ nested while
'''

def star_pattern(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print('*', end='')
            j += 1
        print()
        i += 1

# star_pattern(4)


'''
🧾 ข้อ 3
รับตัวเลขทีละบรรทัด
แต่ละบรรทัดรับได้หลายตัว
จบเมื่อพิมพ์ END
ให้นับว่ารับตัวเลขทั้งหมดกี่ตัว
(ใช้ nested while)
'''

def count_numbers():
    count = 0
    while True:
        line = input('nums: ').strip()
        if line.upper() == 'END':
            break
        nums = line.split()
        j = 0
        while j < len(nums):
            count += 1
            j += 1
    return count
print(count_numbers())