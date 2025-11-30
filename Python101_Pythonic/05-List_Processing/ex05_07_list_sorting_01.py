import time

all_test_data = {
    'sort_1': ["A=50, B=20, C=80, D=40"],  # เรียงคะแนนน้อยไปมาก
    'sort_2': ["Somsak=165, Somchai=180, Manee=150"], # เรียงความสูง (เอาคนเตี้ยสุดขึ้นก่อน)
    'sort_3': ["Apple=35, Durian=150, Banana=20"] # เรียงราคาสินค้า (แพงสุดขึ้นก่อน)
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

'''
แบบฝึกหัด Sorting (สไตล์ป๋า)
ข้อที่ 1: จัดลำดับคะแนน (Low to High) โจทย์: รับข้อมูล ชื่อ=คะแนน แล้วเรียงจากคะแนนน้อยไปมาก

'''

def sort_scores():
    print('--- ข้อ 1: เรียงคะแนน (น้อย->มาก) ---')
    raw_data = input_test('Data: ').split(", ")
    data_list = []
    
    # 1. วนลูปแกะข้อมูล (แบบ For Loop ที่ป๋าชอบ)
    for item in raw_data:
        name, score = item.split('=')
        data_list.append([int(score), name])

    # 2. เรียงลำดับ
    data_list.sort()
    
    # 3. แสดงผล (เฉพาะชื่อ)
    for score, name in data_list:
        print(name, score)
    
mock_inputs = list(all_test_data['sort_1'])
sort_scores()
print('\n')


'''
ข้อที่ 2: เรียงความสูง (Low to High) โจทย์: รับข้อมูล ชื่อ=ความสูง เรียงจากเตี้ยไปสูง
'''

def sort_height():
    print('--- ข้อ 2: เรียงความสูง ---')
    raw_data = input_test('Data: ').split(", ")
    heights = []
    
    for item in raw_data:
        name, heig = item.split('=')
        heights.append([int(heig), name])
    
    heights.sort()

    for no, [heig, name] in enumerate(heights):
        print(no+1, name, heig)
    
    print('เรียงแล้ว:', heights)

mock_inputs = list(all_test_data['sort_2'])
sort_height()
print('\n')

'''
ข้อที่ 3: จัดสินค้าราคาแพง (High to Low) โจทย์: รับ สินค้า=ราคา เรียงจาก แพงที่สุด ไปถูกที่สุด Hint: ตอน sort() เสร็จ ให้ใช้ [::-1] ตอนวนลูป print หรือใช้ .sort(reverse=True) ก็ได้
'''

def sort_price():
    print('--- ข้อ 3: เรียงราคา (แพง->ถูก) ---')
    raw_data = input_test('Data: ').split(", ")
    products = []
    
    # 1. แกะและสลับ (เอา price ขึ้นหน้า)
    for item in raw_data:
        name, price = item.split('=')
        products.append([float(price), name])

    # 2. เรียงลำดับ
    products.sort()    

    # 3. แสดงผลย้อนกลับ (แพงสุดขึ้นก่อน)
    for price, name in products[::-1]:
        print(price, name)

    # ฝึกทำแบบ list comp
    products_comp = [[float(price), name] for name, price 
                     in [item.split('=') for item in raw_data]]
    
    products_comp.sort(reverse=True)
    print('-'*40)
    for no, [price, name] in enumerate(products_comp):
        print(no+1, name, price)

    
    
mock_inputs = list(all_test_data['sort_3'])
sort_price()
print('\n')
''''''