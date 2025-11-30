import time
import random

all_test_data = {
    'm_1': ["A B C D E"],             # หา Z (ไม่มีในลิสต์) ต้องไม่ Error
    'm_2': ["10 20 99 30 99 40"],     # เปลี่ยนเลข 99 เป็น -1 "ทุกตัว"
    'm_3': ["apple banana apple orange"], # ลบคำว่า apple ออก "ให้หมด"
    'm_4': ["Somchai 80 Somsak 45"],  # แก้คะแนน Somsak เป็น 50 (ใช้ index ช่วย)
    'm_5': ["1 2 3 4 5"]              # สลับหัวท้าย (Swap)
}

mock_inputs = []
def fake_input(prompt_text):
    print(prompt_text, end='')
    time.sleep(0.5)
    if mock_inputs:
        val = mock_inputs.pop(0)
        print(val)
        return val
    return ''

input_test = fake_input


'''ข้อที่ 1: ค้นหาแบบกันกระสุน (Safe Index) 
โจทย์: รับชื่อที่ต้องการค้นหา ถ้ามีให้บอก index ถ้าไม่มีให้บอก "Not Found" 
(ห้ามให้โปรแกรม Error เด็ดขาด) Hint: ใช้ if ... in ... เช็คก่อนเรียก index'''

def safe_find():
    print('--- ข้อ 1: หาแบบไม่ Error ---')
    data = input_test('Data: ').split()
    target = 'Z'
    
    # เขียนโค้ดป้องกัน Error ตรงนี้
    if target in data:
        check_index = data.index(target)
    else:
        check_index = 'Not found'
        
    print(f'Target: {target} index: {check_index}')
    
mock_inputs = list(all_test_data['m_1'])
safe_find()
print('============ End Function ============\n')

'''ข้อที่ 2: เปลี่ยนร่างทุกตัว (Replace All) โจทย์: มีเลข 99 (ค่าขยะ) ปนอยู่หลายตัว 
จงเปลี่ยน 99 ให้เป็น -1 ให้หมดทุกตัว 
Hint: ใช้ List Comprehension [... if ... else ...] 
สร้างลิสต์ใหม่ทับลิสต์เดิมง่ายสุดครับ'''

def replace_all():
    print('--- ข้อ 2: เปลี่ยน 99 เป็น -1 ---')
    data = [int(x) for x in input_test('Data: ').split()]

    now_data = [-1 if x == 99 else x for x in data]

    print('Now Data:', now_data)

mock_inputs = list(all_test_data['m_2'])
replace_all()
print('\n')

'''ข้อที่ 3: กำจัดจุดอ่อน (Remove All) 
โจทย์: ลบคำว่า apple ออกจากลิสต์ให้เกลี้ยง 
Hint: ใช้ List Comprehension [x for x in data if x != 'apple']
(สร้างลิสต์ใหม่ที่มีแต่ตัวที่ไม่ใช่ apple)'''

def remove_apple():
    print('--- ข้อ 3: ลบ apple ---')
    data = input_test('Data: ').split()

    clean_data = [d for d in data if d.lower() != 'apple']

    print(f'Clean Data: {' '.join(clean_data)}')

mock_inputs = list(all_test_data['m_3'])
remove_apple()
print('\n')

'''ข้อที่ 4: แก้ข้อมูลเฉพาะจุด (Modify by Index) 
โจทย์: เราเจอว่า "Somsak" คะแนนผิด! จงหา index ของ "Somsak" 
แล้วแก้คะแนน (ตัวถัดไปคือ index + 1) ให้เป็น 50 
Hint: หา idx ของ Somsak ก่อน แล้วใช้ data[idx + 1] = 50'''

def fix_score():
    data = input_test('Score: ').split()
    name = 'Somsak'
    idx = data.index(name)
    data[idx +1 ] = 50

    print('Update:', data)

mock_inputs = list(all_test_data['m_4'])
fix_score()
print('\n')

'''ข้อที่ 5: สลับร่างสร้างรัก (Swap) 
โจทย์: จงสลับค่า "ตัวแรก" กับ "ตัวสุดท้าย" ของลิสต์ 
Hint: Python สลับค่าง่ายมาก a, b = b, a หรือ 
data[0], data[-1] = data[-1], data[0]'''

def swap_head_tail():
    print('--- ข้อ 5: สลับหัวท้าย ---')
    data = input_test('Data: ').split()

    data[0], data[-1] = data[-1], data[0]

    print('Swapped:', data)
 
mock_inputs = list(all_test_data['m_5'])
swap_head_tail()