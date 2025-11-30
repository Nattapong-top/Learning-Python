import time

'''โปรแกรมจำลองการกรอกข้อมูล (เอาไว้ทำสอบการทำงานของโปรแกรม)'''
all_test_data = {
    'ex_1': ["5", "10.5", "45.0", "60.5", "30.0", "75.2"], # สำหรับข้อ 1
    'ex_2': ["Cat", "Elephant", "Dog", "Bird", "Crocodile", "quit"], # สำหรับข้อ 2
    'ex_3': ["12 45 2 9 100 33 58"], # สำหรับข้อ 3
    'ex_4': ["Somchai 80 Somsak 55 Somsri 72 Somying 48"], # สำหรับข้อ 4
    'ex_5': ["4", "2", "5", "10", "3"] # สำหรับข้อ 5
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
'''โปรแกรมจำลองการกรอกข้อมูล (เอาไว้ทำสอบการทำงานของโปรแกรม)'''

'''โจทย์แบบฝึกหัด
ข้อที่ 1: กรองคนสอบผ่าน (Basic Loop + Condition)
โจทย์: รับค่า n (จำนวนรอบ) จากนั้นรับคะแนน (float) ตามจำนวนรอบ 
ให้เก็บคะแนนลงในลิสต์ x เฉพาะคะแนนที่มากกว่าหรือเท่ากับ 50.0 เท่านั้น (ใครตกไม่เอา) 
ใช้ข้อมูล: all_test_data['ex_1']
ผลลัพธ์ที่ต้องการ: [60.5, 75.2]'''
def pass_the_exam():
    
    x = []
    n = input_test('Students: ')

    for i in range(1, int(n)+1):
        scores = input_test('scores: ')
        x.append(float(scores))
    
    x = [num for num in x if num >= 50]
    print('exam pass:', x)

mock_inputs = list(all_test_data['ex_1'])
# pass_the_exam()
print('============ End Function ============\n')

'''ข้อที่ 2: สัตว์ตัวใหญ่ (While + String Length)
โจทย์: รับชื่อสัตว์ (String) ไปเรื่อยๆ จนกว่าจะเจอคำว่า 'quit' 
ให้เก็บชื่อสัตว์ลงในลิสต์ x เฉพาะชื่อที่มีความยาวมากกว่า 3 ตัวอักษร 
(เช่น Cat ไม่เอา, Elephant เอา) 
คำใบ้: ใช้ len(ตัวแปร) > 3 เพื่อเช็คความยาว
ใช้ข้อมูล: all_test_data['ex_2']
ผลลัพธ์ที่ต้องการ: ['Elephant', 'Bird', 'Crocodile']'''
def big_animal():
    x = []
    animal = input_test('animal name: ')
    while animal != 'quit':
        if len(animal) > 3:
            x.append(animal)
        
        animal = input_test('animal name: ')

    print('len > 3', x)

mock_inputs = list(all_test_data['ex_2'])
# big_animal()
print('============ End Function ============\n')


'''ข้อที่ 3: แยกเลขคี่ (Split + Modulo)
โจทย์: รับชุดตัวเลขจำนวนเต็ม 1 บรรทัด (คั่นด้วยช่องว่าง) ให้แปลงเป็น int 
และเก็บลงในลิสต์ x เฉพาะที่เป็นเลขคี่ (Odd Number)
คำใบ้: เลขคี่คือเลขที่หาร 2 แล้วเหลือเศษ 1 (i % 2 == 1)
ใช้ข้อมูล: all_test_data['ex_3']
ผลลัพธ์ที่ต้องการ: [45, 9, 33]'''

def split_modulo():
    n = input_test('num: ').split()
    x = [int(i) for i in n if int(i) % 2 == 1]
    print('Odd Number:', x)

mock_inputs = list(all_test_data['ex_3'])
# split_modulo()
print('============ End Function ============\n')


'''ข้อที่ 4: แยกชื่อกับคะแนน (Slicing ขั้นสูง)
โจทย์: รับข้อมูลบรรทัดเดียว เป็น ชื่อ สลับกับ คะแนน 
(เช่น ชื่อ1 คะแนน1 ชื่อ2 คะแนน2 ...) 
จงแยกเก็บข้อมูลลง 2 ลิสต์:
names เก็บรายชื่อ
scores เก็บเป็นตัวเลข int
ใช้ข้อมูล: all_test_data['ex_4']
ผลลัพธ์ที่ต้องการ:
names = ['Somchai', 'Somsak', 'Somsri', 'Somying']
scores = [80, 55, 72, 48]'''
def name_scores_slicing():
    data = input_test('data: ').split()

    names = data[0::2]
    scores = [int(e) for e in data[1::2]]

    print('names:', names)
    print('scores: ', scores)

mock_inputs = list(all_test_data['ex_4'])
name_scores_slicing()
print('============ End Function ============\n')

'''ข้อที่ 5: ยกกำลังสอง (Map / Math)
โจทย์: รับค่า n (จำนวนรอบ) จากนั้นรับตัวเลข int ตามจำนวนรอบ 
เก็บใส่ลิสต์ x จากนั้นให้สร้างลิสต์ใหม่ชื่อ y โดยสมาชิกใน y คือค่าของ x ยกกำลังสอง
ใช้ข้อมูล: all_test_data['ex_5']
ผลลัพธ์ที่ต้องการ:
x = [2, 5, 10, 3]
y = [4, 25, 100, 9]'''
def map_math_pow_2():
    x = []
    n = int(input_test('Round: '))

    for i in range(n):
        num = int(input_test('num: '))
        x.append(num)
    
    y = [pow(i, 2) for i in x]

    print('List x', x)
    print('List y', y)

mock_inputs = list(all_test_data['ex_5'])
map_math_pow_2()
print('============ End Function ============\n')

