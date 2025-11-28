import time

all_test_data = {
    'q_1': ["10 -5 20 -1 30"],        # นับจำนวนเลขบวก
    'q_2': ["50 60 70 80", "50 40 70 80"], # ตรวจว่าสอบผ่าน "ทุกคน" ไหม (เกณฑ์ 50)
    'q_3': ["A B C D", "A X C Z"],    # ตรวจเฉลยข้อสอบ (เทียบ 2 ลิสต์)
    'q_4': ["10 20 30 40", "10 50 20 30"] # ตรวจว่าข้อมูลเรียงน้อยไปมากหรือไม่
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

def count_positives():
    print('--- ข้อ 1: นับจำนวนเลขบวก ---')
    nums = [int(x) for x in input_test('Nums: ').split()]
    
    count = sum(1 for n in nums if n > 0)

    print('Count:', count)

mock_inputs = list(all_test_data['q_1'])
count_positives()
print('\n')

def check_all_pass():
    print('--- ข้อ 2: ผ่านยกห้องไหม? ---')
    scores = [int(x) for x in input_test('Scores: ').split()]
    
    # เขียนโค้ดบรรทัดเดียวตรงนี้
    result = all(x >= 50 for x in scores)

    print('All pass:', result)

mock_inputs = list(all_test_data['q_2']) # ลองเปลี่ยนค่าเล่นดูได้ครับ
check_all_pass() # รอบแรกควร True
check_all_pass() # รอบสองควร False
print('\n')

def check_answers():
    print('--- ข้อ 3: ตรวจคะแนนสอบ ---')
    solution = input_test('Solution: ').split()
    student = input_test('Student : ').split()
    
    # เขียนโค้ดบรรทัดเดียวตรงนี้ (นับคู่ที่เหมือนกัน)
    score = sum(1 for x, y in zip(solution, student) if x == y)

    print('Score:', score)

mock_inputs = list(all_test_data['q_3'])
check_answers()
print('\n')


'''ข้อที่ 4: เรียงลำดับหรือยัง (ใช้ zip หรือ sorted) 
โจทย์: ตรวจสอบว่าตัวเลขในลิสต์ เรียงจาก น้อยไปมาก ถูกต้องหรือไม่ 
คำใบ้: เลือกใช้ท่าไม้ตายที่ชอบได้เลย ระหว่าง nums == sorted(nums)
หรือ all(... zip(nums, nums[1:]))'''

def is_sorted():
    print('--- ข้อ 4: เรียงลำดับหรือไม่ ---')
    nums = [int(x) for x in input_test('Nums: ').split()]
    
    # เขียนโค้ดบรรทัดเดียวตรงนี้
    result = 'YES' if nums == sorted(nums) else 'NO'

    print('Is Sorted:', result)

mock_inputs = list(all_test_data['q_4'])
is_sorted() # รอบแรก True
is_sorted() # รอบสอง False
print('\n')