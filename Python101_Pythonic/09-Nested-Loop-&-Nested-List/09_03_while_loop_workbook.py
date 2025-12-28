'''
📘 บทฝึก: while loop (พื้นฐาน)
'''

'''
🧾 ข้อ 1
จงพิมพ์เลข 1 ถึง n โดยใช้ while
'''

def while_count(n):
    i = 1    
    result = []
    while i < n+1:
        result.append(i)
        i += 1
    return result

print(while_count(5))


'''
🧾 ข้อ 2
รับ input ทีละบรรทัด
จนกว่าจะเจอคำว่า "END"
แล้วนับว่ามีกี่บรรทัด (ไม่รวม END)
'''

def count_lines():
    count = 0
    while True:
        line = input('count: ')
        if line.upper() == 'END':
            break
        count += 1
    return count
# print(count_lines())

'''
🧾 ข้อ 3
จงหาผลรวมของตัวเลขใน list โดยใช้ while
'''

def sum_list(nums):
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    return total
print(sum_list([1, 2, 3, 4]))
