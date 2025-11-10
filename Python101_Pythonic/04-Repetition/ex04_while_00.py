'''
ให้เขียนโปรแกรมรับจำนวนเต็ม n จาก input 
เพื่อแสดงจำนวนเต็มคี่ตั้งแต่ 1 ถึงจำนวนคี่ที่ไม่เกิน n 
(โดยใช้วงวน while)
'''

def input_n_01():

    n = int(input())
    count = 0

    while count < n + 1:
        print(count)
        count += 1
# input_n_01()

'''
ข้อมูลที่ input มีบรรทัดแรกเป็นจำนวนเต็ม n ตามด้วยอีก n 
บรรทัดเป็นจำนวนเต็ม d0, d1, ..., dn-1 บรรทัดละจำนวน 
จงเขียนโปรแกรมอ่านข้อมูลจาก input (โดยใช้วงวน while) 
เพื่อหาผลรวมของ d0, d1, ..., dn-1
'''
def input_n_sum_n():
    n = int(input('ป้อนจำนวนครั้ง: '))
    count = 1
    total_sum = 0

    while count < n+1:
        d = int(input(f'ป้อนตัวเลข ครั้งที่ {count}: '))
        total_sum += d
        count += 1
    print(f'จำนวนครั้ง {n}, ผลรวม {total_sum}')
# input_n_sum_n()

'''
ข้อมูลจาก input เป็นจำนวนเต็ม บรรทัดละจำนวน 
จงเขียนโปรแกรมรับข้อมูลจาก input (โดยใช้วงวน while) 
เพื่อหาผลรวมของจำนวนที่อ่านเข้ามา จนพบจำนวนลบ (ไม่รวมจำนวนลบ)
'''
def input_num_n():
    total_sum = 0
    count = 1
    n = int(input(f'ป้อนตัวเลข ครั้งที่: {count}: '))

    while n > -1:
        total_sum += n
        count += 1
        n = int(input(f'ป้อนตัวเลข ครั้งที่: {count}: '))

    print(f'ผลรวม: {total_sum}')
input_num_n()