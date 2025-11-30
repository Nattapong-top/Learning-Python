import time

'''โปรแกรมจำลองการกรอกข้อมูล'''
all_test_data = {
    'q_1': ["Apple Banana Cherry Date Elderberry"], # นับจำนวนตัวอักษร
    'q_2': ["15 22 8 19 30 4 11"],                 # หาเลขคู่
    'q_3': ["45 60 32 80 49 50"],                 # ตัดเกรด (>=50 ผ่าน)
    'q_4': ["Book 250 Pen 30 Ruler 15 Eraser 10"], # ดึงเฉพาะราคาที่เป็นตัวเลข
    'q_5': ["100 200 500 1000"]                   # คำนวณราคาบวก VAT 7%
}

mock_inputs = []

def fake_input(prompt_text):
    print(prompt_text, end='')
    time.sleep(0.5)
    if mock_inputs:
        val = mock_inputs.pop(0)
        return val

input_test = fake_input

'''ข้อที่ 1: ความยาวของคำ โจทย์: รับชื่อผลไม้เข้ามาเป็นลิสต์ ให้สร้างลิสต์ y เก็บ จำนวนตัวอักษร ของแต่ละคำ'''
print()
def count_chars():
    print('---- ข้อ 1 นับจำจำนวนตัวอักษร')
    fult = input_test('fult: ').split()
    count_name = [len(e) for e in fult]

    print('fule:', fult)
    print('count name:', count_name)

mock_inputs = list(all_test_data['q_1'])
count_chars()
print('============ End Function ============\n')


'''ข้อที่ 2: คัดเลือกเลขคู่ (Even Numbers) โจทย์: รับชุดตัวเลขเข้ามา ให้สร้างลิสต์ y ที่เก็บเฉพาะ เลขคู่ เท่านั้น (เลขที่หาร 2 ลงตัว)'''

def filter_evens():
    print('--- ข้อ 2: คัดเฉพาะเลขคู่ ---')
    nums = input_test('Num: ').split()
    
    y = [int(i) for i in nums if int(i) % 2 == 0]

    print('nums', nums)
    print('Evens:', y)

mock_inputs = list(all_test_data['q_2'])
filter_evens()
print('============ End Function ============\n')


'''ข้อที่ 3: ตรวจผลสอบ (Pass/Fail) โจทย์: รับคะแนนสอบเข้ามา ให้สร้างลิสต์ y ที่เก็บข้อความว่า "Pass" ถ้าคะแนน >= 50 และ "Fail" ถ้าคะแนนน้อยกว่า 50'''

def check_grades():
    print('--- ข้อ 3: ตรวจผลสอบ (>=50 Pass) ---')
    scores_str = input_test('Scores: ').split()
    scores = [int(s) for s in scores_str]
    
    y = ['Pass' if score >= 50 else 'Fail' for score in scores]

    print('scores', list(scores))
    print('Results:', y)

mock_inputs = list(all_test_data['q_3'])
check_grades()
print('============ End Function ============\n')


'''ข้อที่ 4: นักสืบตัวเลข โจทย์: ข้อมูลที่รับมามีทั้งชื่อสินค้าและราคาปนกัน (เช่น "Book 250 ...") ให้สร้างลิสต์ y ที่เก็บเฉพาะข้อมูลที่ เป็นตัวเลข เท่านั้น (เพื่อเตรียมเอาไปคำนวณต่อ)'''

def extract_numbers():
    print('--- ข้อ 4: ดึงเฉพาะตัวเลข ---')
    data = input_test('Data: ').split()
    
    nums = [i for i in data if i.isdigit()]

    print('data', data)
    print('Prices only:', nums)

mock_inputs = list(all_test_data['q_4'])
extract_numbers()
print('============ End Function ============\n')



'''ข้อที่ 5: คำนวณราคารวม VAT โจทย์: รับราคาสินค้าเข้ามา ให้สร้างลิสต์ y ที่เป็นราคาสุทธิ (ราคาต้น + VAT 7%) สูตร: ราคา * 1.07'''

def price_with_vat():
    print('--- ข้อ 5: ราคารวม VAT 7% ---')
    prices = input_test('Prices: ').split()

    y = [round(float(i) * 1.07, 2) for i in prices]
    
    print(prices)
    print('Net Prices:', y)

mock_inputs = list(all_test_data['q_5'])
price_with_vat()
print('============ End Function ============\n')
