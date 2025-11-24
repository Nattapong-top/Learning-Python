import time

'''โปรแกรมจำลองการกรอกข้อมูล (เอาไว้ทำสอบการทำงานของโปรแกรม)'''
all_test_data = {
    'ex_1': ["12 45 2 9 100 33 58"], # สำหรับข้อ 1
    'ex_2': ["12 -45 2 9 -100 33 -58"], # สำหรับข้อ 2
    'ex_3': ["12 -45 2 9 -100 33 -58"], # สำหรับข้อ 3
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

'''แบบฝึกหัด 5-4 ข้อที่ 1
กำหนดให้มีตัวแปร x เป็นลิสต์เก็บจำนวนเต็มมาให้แล้ว จงสร้างลิสต์ y ที่เก็บค่ากำลังสองของแต่ละตัวใน x ในลำดับเดียวกับ x และแสดงค่าของ y ด้วย'''
def x_y_pow_2():
    x = input_test('num: ').split()
    y = [int(i) ** 2 for i in x]

    print('y**2 in x:', y)

mock_inputs = list(all_test_data["ex_1"])
x_y_pow_2()
print('============ End Function ============\n')
    

'''แบบฝึกหัด 5-4 ข้อที่ 2
กำหนดให้มีตัวแปร x เป็นลิสต์เก็บจำนวนเต็มมาให้แล้ว จงสร้างลิสต์ y ที่มีแต่ค่าที่ใน x ที่เป็นจำนวนบวกในลำดับเดียวกับ x และแสดงค่าของ y ด้วย'''
def num_positive():
    x = input_test('num: ').split()
    y = [int(i) for i in x if int(i) > 0]

    print('x positive:', y)

mock_inputs = list(all_test_data['ex_2'])
num_positive()
print('============ End Function ============\n')


'''แบบฝึกหัด 5-4 ข้อที่ 3
กำหนดให้มีตัวแปร x เป็นลิสต์เก็บจำนวนเต็มมาให้แล้ว จงสร้างลิสต์ y ที่เก็บค่ารากที่สองของแต่ละตัวใน x (เลือกทำกับค่าใน x ที่เป็นจำนวนไม่ติดลบเท่านั้น) ในลำดับเดียวกับ x และแสดงค่าของ y ด้วย'''
def e_root_2():
    n = input_test('num: ').split()
    x = [int(i) for i in n]
    y = [e ** 0.5 for e in x if e >= 0 ]
    print('root 2:', y)

mock_inputs = list(all_test_data['ex_3'])
e_root_2()
print('============ End Function ============\n')


