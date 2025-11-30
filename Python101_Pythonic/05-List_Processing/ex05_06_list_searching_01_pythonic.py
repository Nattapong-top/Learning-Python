import time
import random

all_test_data = {
    'q_1': ["Somchai Somsak Somsri Mana Manee"],   # รายชื่อแขก (หาว่ามี "Mana" ไหม)
    'q_2': ["A01 A02 A03 B01 B02"],               # คิวรอรับบริการ (หาว่า "B01" อยู่คิวที่เท่าไร)
    'q_3': ["10 50 10 20 10 30"],                 # นับจำนวนเหรียญ 10
    'q_4': ["45 80 32 99 55"],                    # หาตำแหน่งของคนได้คะแนนสูงสุด (Max Index)
    'q_5': ["10 20 -1 30 -1 40"]                  # หาตำแหน่งของข้อมูลที่เสีย (ค่า -1 ตัวแรก)
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
'''------------------------------------------'''

'''แบบฝึกหัด 5-6: List Searching
ข้อที่ 1: ตรวจรายชื่อ (Existence Check) 
โจทย์: รับรายชื่อแขกทั้งหมดมา และรับชื่อที่ต้องการค้นหา 
(ในที่นี้ให้ค้นหา "Mana") ถ้าเจอให้พิมพ์ "Found" ถ้าไม่เจอพิมพ์ "Not Found" 
Hint: ใช้ if ... in ...'''

def check_guest():
    print('--- ข้อ 1: ตรวจรายชื่อ ---')

    guest = input_test('Guest: ').split()
    target = random.choice(['Mana','Papa','Somsak'])

    print('Searching', target)

    print('Found' if target in guest else 'Not found')

    # if target in guest:
    #     print('Found')
    # else:
    #     print('Not found')

mock_inputs = list(all_test_data['q_1'])
check_guest()
print('\n')

'''ข้อที่ 2: สอบถามคิว (Finding Index) 
โจทย์: รับรายการคิวทั้งหมด และต้องการรู้ว่า "B01" อยู่ลำดับที่เท่าไร 
(ลำดับที่มนุษย์เข้าใจ คือเริ่มที่ 1 ไม่ใช่ 0) 
Hint: ใช้ .index() แล้วอย่าลืม +1'''

def find_queue():
    print('--- ข้อ 2: สอบถามคิว')
    queues = input_test('Queues: ').split()
    my_q = 'B01'

    # print(queues.index(q) for q in queues if q == my_q)
    # q_order = [queues.index(q)+1 for q in queues if q == my_q]
    # print('Queue:', q_order)

    if my_q in queues:
        print('Queue:', queues.index(my_q)+1)
    
mock_inputs = list(all_test_data['q_2'])
find_queue()
print('\n')

'''ข้อที่ 3: นับเหรียญ (Counting) 
โจทย์: รับลิสต์ของเหรียญทั้งหมดเข้ามา อยากรู้ว่ามีเหรียญ "10" อยู่กี่เหรียญ 
Hint: ข้อมูลที่รับมาจะเป็น String ("10") ใช้ .count() ได้เลย'''

def count_coin():
    print('--- ข้อ 3: นับเหรียญ ---')
    coin = input_test('Coins: ').split()
    target = '10'

    amount = coin.count(target)

    print(f'เจอเหรียญ: {target} จำนวน: {amount} เหรียญ')

mock_inputs = list(all_test_data['q_3'])
count_coin()
print('\n')

'''ข้อที่ 4: ใครเก่งสุด? (Index of Max) 
โจทย์: รับคะแนนสอบมา จงหาว่าคะแนนสูงสุด "อยู่ที่ลำดับ index ไหน" 
Hint: หาค่า max() ออกมาก่อน แล้วค่อยเอาค่านั้นไปหา .index()'''

def find_max_index():
    print('--- ข้อ 4: ตำแหน่งคนเก่งสุด ---')
    scores = [int(i) for i in input_test('Scores: ').split()]

    max_val = max(scores)

    max_index = scores.index(max_val)

    print(f'คะแนนสูงสุดคือ {max_val} อยู่ที่ index {max_index}')

mock_inputs = list(all_test_data['q_4'])
find_max_index()
print('\n')


'''ข้อที่ 5: หาของเสีย (Linear Search / First Match) 
โจทย์: ข้อมูลที่รับมามีเลข -1 ปนอยู่ (ซึ่งแปลว่าข้อมูลเสีย error) 
จงหา Index แรกสุด ที่เจอ -1 แล้วหยุดทันที 
Hint: ใช้ .index(-1) ก็ได้ หรือถ้าจะฝึก Loop ให้ใช้ break เมื่อเจอ'''

def find_error():
    print('--- ข้อ 5: หา Error แรก ---')
    data = [int(x) for x in input_test('Data: ').split()]
    
    # ลองใช้ .index() ในการหาค่า -1
    # ข้อเสียวิธีนี้คือ ถ้า ไม่มี index โปรแกรมจะบึ้ม
    error_idx = data.index(-1)
    # for d in data:
    #     if d == -1:
    #         error_idx = data.index(d)
    #         break
    
    print(f"เจอข้อมูล error ที่ index: {error_idx}")

mock_inputs = list(all_test_data['q_5'])
find_error()
print('\n')