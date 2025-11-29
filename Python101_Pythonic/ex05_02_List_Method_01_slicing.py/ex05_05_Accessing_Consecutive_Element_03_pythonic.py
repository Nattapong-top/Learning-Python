import time

all_test_data = {
    'h_1': ["  apple  ", "banana ", "  CHERRY", " date "], # Clean ข้อมูล
    'h_2': ["level kayak hello madam world"],               # หาคำที่อ่านหน้าหลังเหมือนกัน (Palindrome)
    'h_3': ["10 20 30", "2 0.5 3"],                         # คำนวณคะแนนถ่วงน้ำหนัก (Weighted Score)
    'h_4': ["10 15 22 30 50"],                              # หา "ระยะห่าง" ระหว่างตัวเลข (Diff)
    'h_5': ["P@ssw0rd1234", "weakpass", "StrongP@ss1", "no"] # กรองรหัสผ่านที่ปลอดภัย
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

'''แบบฝึกหัด 5 ข้อ (Hard Mode)
ข้อที่ 1: นักจัดการข้อมูล (Data Cleaning) 
โจทย์: ข้อมูลที่รับมาเละเทะมาก มีช่องว่างข้างหน้าข้างหลัง 
และตัวเล็กตัวใหญ่ปนกัน จงสร้างลิสต์ใหม่ที่ ตัดช่องว่างออก (strip) 
และ แปลงเป็นตัวพิมพ์ใหญ่ (upper) Hint: s.strip().upper()'''

def clean_data():
    print('--- ข้อ 1: Clean Data ---')
    raw_data = list(all_test_data['h_1']) # ดึงลิสต์มาตรงๆ เลย ไม่ต้อง split เพราะเป็นลิสต์อยู่แล้ว
    print('Raw:', raw_data)
    
    # เขียนโค้ดบรรทัดเดียว (Combo: strip + upper)
    clean_list = [ c.strip().upper() for c in raw_data ]

    print('Cleaned:', clean_list)

# หมายเหตุ: ข้อนี้ mock input ไม่ต้องใช้ fake_input ก็ได้ครับ ผมดึงจาก dict มาให้เลยเพื่อความง่าย
clean_data()
print('\n')

'''ข้อที่ 2: มนุษย์หน้าหลัง (Palindrome) 
โจทย์: รับประโยคเข้ามา แยกเป็นคำๆ แล้วนับว่ามีกี่คำที่ 
"อ่านจากหน้าไปหลัง และหลังมาหน้า เหมือนกัน"
(เช่น level, kayak) Hint: 
การกลับด้านข้อความใน Python ใช้ word[::-1]'''

def count_palindromes():
    print('--- ข้อ 2: Palindrome Count ---')
    words = input_test('Word: ').split()

    count = sum(1 for c in words if c[0:] == c[0:][::-1])

    print('Palindromes:', count)

mock_inputs = list(all_test_data['h_2'])
count_palindromes()
print('\n')

'''ข้อที่ 3: คะแนนถ่วงน้ำหนัก (Dot Product) 
โจทย์: รับข้อมูล 2 ชุด ชุดแรกคือ คะแนน (Score) ชุดสองคือ น้ำหนัก (Weight) 
จงคำนวณ ผลรวมของ (คะแนน x น้ำหนัก) ทั้งหมด 
สูตร: (10*2) + (20*0.5) + (30*3) 
Hint: ใช้ zip จับคู่ แล้วคูณกัน แล้วค่อย sum ทีเดียว'''
def weighted_score():
    print('--- ข้อ 3: Weighted Score ---')
    scores = [float(x) for x in input_test('Scores: ').split()]
    weight = [float(x) for x in input_test('Weight: ').split()]

    total = sum(s*h for s, h in zip(scores, weight))

    print('Total Score:', total)

mock_inputs = list(all_test_data['h_3'])
weighted_score()
print('\n')

'''ข้อที่ 4: หาความห่าง (Differences) โจทย์: รับชุดตัวเลขที่เรียงกันมา 
จงสร้างลิสต์ใหม่ที่เก็บ "ผลต่าง" ของตัวเลขที่อยู่ติดกัน 
ตัวอย่าง: [10, 15, 22] -> 15-10=5, 22-15=7 -> ผลลัพธ์ [5, 7] 
Hint: ใช้ zip(nums[1:], nums) แล้วเอา ตัวหลัง - ตัวหน้า'''

def find_diff():
    print('--- ข้อ 4: Differences ---')
    nums = [int(x) for x in input_test('Nums: ').split()]

    diffs = [b - a for b, a in zip(nums[1:], nums)]

    print('Diffs:', diffs)

mock_inputs = list(all_test_data['h_4'])
find_diff()
print('\n')


'''ข้อที่ 5: รปภ. คัดกรองรหัสผ่าน (Complex Filter) 
โจทย์: มีลิสต์รหัสผ่าน จงกรองเอาเฉพาะรหัสผ่านที่ "ปลอดภัย" 
โดยมีเงื่อนไขว่าต้อง ยาวมากกว่า 6 ตัวอักษร และ มีตัวเลขผสมอยู่ด้วย 
Hint: len(s) > 6 และเช็คตัวเลขใช้ any(c.isdigit() for c in s) '''

def filter_passwords():
    print('--- ข้อ 5: Password Filter ---')
    passwords = list(all_test_data['h_5'])
    print('All Passwords:', passwords)

    valid_pass = [ pw for pw in passwords 
                  if len(pw) > 6 and any(c.isdigit() for c in pw)]

    print('Valid Pass:', valid_pass)
filter_passwords()
print('\n')