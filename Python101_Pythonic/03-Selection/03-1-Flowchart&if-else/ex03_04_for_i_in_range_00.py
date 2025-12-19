'''
อ่านจำนวนเต็ม a, b และ c จาก input แล้วแสดงจำนวนเต็มที่มีค่า a, a+c, a+2c, ... บรรทัดละหนึ่งค่า
โดยจะหยุดแสดงเมื่อค่าที่คำนวณมากกว่าหรือเท่ากับ b เช่น a=2, b=7, c=2 
จะแสดง 2, 4 และ 6 บรรทัดละค่า
'''
def for_start_end_step():
    a, b, c = map(int, input('ป้อนตัวเลข 3 ชุด แบ่งด้วยวรรค: ').split())

    for i in range(a, b, c):
        print(i)
# for_start_end_step()

'''
อ่านจำนวนเต็มไม่ติดลบ m จาก input แล้วแสดงเฉพาะจำนวนเต็มคู่ที่มีค่าตั้งแต่ -m จนถึง m บรรทัดละหนึ่งค่า
'''
def for_negative_to_positive():
    m = int(input('ป้อนตัวเลขจำนวนเต็มไม่ติดลบ: '))

    for i in range(-m, m+1):
        if i % 2 == 0:
            print(i)
# for_negative_to_positive()

'''
อ่านจำนวนเต็ม n จาก input แล้วเขียนคำสั่งเพื่อคำนวณและแสดงค่าของ 
∑ n i = 1 i 5
(โดยใช้วงวน for)'''

def for_sum_power_five():
    n = int(input('ป้อนตัวเลขจำนวนเต็ม: '))

    total = 0
    for i in range(1, n+1):
        total += i**5
    print(f'ผลรวมของ Σ i^5 ตั้งแต่ 1 ถึง {n} คือ {total:,}')
for_sum_power_five()