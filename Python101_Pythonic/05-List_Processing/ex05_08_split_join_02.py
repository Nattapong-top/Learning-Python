import time

'''ชุดข้อมูลทดสอบ'''
all_test_data = {
    'sj_1': ["somchai.abc@gmail.com"],      # ดึงชื่อ Domain (gmail.com)
    'sj_2': ["25/12/2025"],                 # เปลี่ยนวันที่เป็นแบบขีด (25-12-2025)
    'sj_3': ["C:/Users/Admin/Documents"],   # เปลี่ยน Path เป็นลูกศร (C: -> Users -> ...)
    'sj_4': ["Somsak 25 Bangkok"],          # สร้างไฟล์ CSV (คั่นด้วยจุลภาค)
    'sj_5': ["Python is very easy"]         # กลับหลังประโยค (easy very is Python)
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

'''ข้อที่ 1: นักแกะอีเมล (Extract Domain)
โจทย์: รับอีเมลเข้ามา จงแยกเอาเฉพาะ "ชื่อเว็บไซต์" ที่อยู่หลังเครื่องหมาย @
Hint: split('@') แล้วเอาตัวสุดท้าย'''
def get_domain():
    print('--- ข้อ 1: Get Domain ---')
    email = input_test('Email: ')
    
    # เขียนโค้ดตรงนี้
    _, domain = email.split('@')
    
    print('Domain:', domain)

mock_inputs = list(all_test_data['sj_1'])
get_domain()
print('\n')


'''ข้อที่ 2: แปลงร่างวันที่ (Date Format)
โจทย์: รับวันที่ที่มี / (เช่น 25/12/2025) จงเปลี่ยนให้เป็นแบบมีขีด - (25-12-2025)
Hint: Split ด้วย / แล้ว Join กลับด้วย -'''
def convert_date():
    print('--- ข้อ 2: Convert Date ---')
    date_str = input_test('Date: ')
    
    # 1. แยกส่วน
    date = date_str.split('/')
    # 2. รวมร่างใหม่
    new_date = '-'.join(date)
    # new_date = '-'.join(date_str.split('/'))
    
    print('New Date:', new_date)

mock_inputs = list(all_test_data['sj_2'])
convert_date()
print('\n')


'''ข้อที่ 3: บอกทาง (Breadcrumb Navigation)
โจทย์: รับ Path ไฟล์คอมพิวเตอร์ (คั่นด้วย /) จงเปลี่ยนให้เป็นป้ายบอกทางสวยๆ คั่นด้วย " > "
Hint: Split ด้วย / แล้ว Join ด้วย " > "'''
def make_breadcrumb():
    print('--- ข้อ 3: Breadcrumb ---')
    path = input_test('Path: ')
    
    # เขียนโค้ดแปลงร่าง
    breadcrumb = '>'.join(path.split('/'))
    
    print('Navigation:', breadcrumb)

mock_inputs = list(all_test_data['sj_3'])
make_breadcrumb()
print('\n')


'''ข้อที่ 4: สร้างไฟล์ CSV (Comma Separated Values)
โจทย์: รับข้อมูลที่คั่นด้วยช่องว่าง (เช่น ชื่อ อายุ จังหวัด) จงเปลี่ยนให้คั่นด้วยลูกน้ำ (,) เพื่อเอาไปใช้ใน Excel
Hint: เหมือนข้อ 2 แต่เปลี่ยนตัวคั่น'''
def create_csv():
    print('--- ข้อ 4: Create CSV ---')
    raw_data = input_test('Data: ')
    
    csv_line = ','.join(raw_data.split())
    
    print('CSV Format:', csv_line)

mock_inputs = list(all_test_data['sj_4'])
create_csv()
print('\n')


'''ข้อที่ 5: ประโยคกลับหลังหัน (Reverse Sentence)
โจทย์: รับประโยคเข้ามา จงเรียง "คำ" ถอยหลัง (ไม่ใช่กลับตัวอักษรนะ แต่กลับลำดับคำ)
เช่น "I love Python" -> "Python love I"
Hint: Split เป็น list -> กลับด้าน List ([::-1]) -> Join กลับเป็นประโยค'''
def reverse_words():
    print('--- ข้อ 5: Reverse Words ---')
    sentence = input_test('Sentence: ')
    
    # # 1. แยกคำ
    # list_words = sentence.split()
    # # 2. กลับด้าน List
    # now_words = list_words[::-1]
    # # 3. รวมร่าง
    # result = ' '.join(now_words)
    result = ' '.join(sentence.split()[::-1])

    
    print('Reversed:', result)

mock_inputs = list(all_test_data['sj_5'])
reverse_words()
print('\n')