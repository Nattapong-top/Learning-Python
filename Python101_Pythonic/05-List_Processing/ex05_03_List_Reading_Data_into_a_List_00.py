import time

'''โปรแกรมจำลองการกรอกข้อมูล (เอาไว้ทำสอบการทำงานของโปรแกรม)'''
all_test_data = {
    'test_set_1': ["5", "10.2", "23.1", "20.2", "19.1", "19.2"],
    'test_set_2': ['10.2', '23.1', '20.2', '19.1', '19.2', 'sdfg', 'end'],
    'test_set_3': ['10 20 30 20 40 10 23 sdfg end'],
    'test_set_4': ['CP Computer CE Civil ME Mechanical EE Electrical IE Industrial']

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


'''แบบฝึกหัด 5-3 
ข้อที่ 1 อ่านข้อมูลจาก input ที่มีลักษณะดังตัวอย่างในรูป 
บรรทัดแรกบอกจำนวนข้อมูลและตามด้วยข้อมูลบรรทัดละจำนวน 
จากตัวอย่าง จงเขียนคำสั่งอ่านเข้ามาเก็บในลิสต์ชื่อ x มีค่าคือ 
[10.2, 23.1, 20.2, 19.1, 19.2]'''
def input_round_n():
    x = []
    n = int(input_test('round: '))

    for i in range(1, n+1):
        e = float(input_test(f'{i} = '))
        x.append(e)
    print('result:', x)

mock_inputs = list(all_test_data['test_set_1'])
# input_round_n()
print('============ End Function ============\n')

'''แบบฝึกหัด 5-3 ข้อที่ 2
อ่านข้อมูลจาก input ที่มีลักษณะดังตัวอย่างในรูป 
บรรทัดแรกบอกจำนวนข้อมูลและตามด้วยข้อมูลบรรทัดละจำนวน จากตัวอย่าง 
จงเขียนคำสั่งอ่านเข้ามาเก็บในลิสต์
ชื่อ x มีค่าคือ [19.2, 19.1, 20.2, 23.1, 10.2]'''
def input_round_n_insert_0():
    x = []
    n = int(input_test('round: '))

    for i in range(1,n+1):
        e = float(input_test(f'{i} num float: '))
        x.insert(0, e)

    print(f'result: {x}')
# input_round_n_insert_0()
print('============ End Function ============\n')

'''อ่านข้อมูลจาก input ที่มีลักษณะดังตัวอย่างในรูป 
คือ มีข้อมูลบรรทัดละจำนวน โดยบรรทัดสุดท้ายเป็นคำว่า end จากตัวอย่าง 
จงเขียนคำสั่งอ่านเข้ามาเก็บในลิสต์ชื่อ x มีค่า
คือ [10.2, 23.1, 20.2, 19.1, 19.2]'''

def while_n_end():
    x = []
    n = input_test('')

    while n != 'end':
        if not n.isalpha():
            x.append(float(n))
        n = input_test('')
    x = x[0::2] + x[1::2]
    print('renow_x:', x)

mock_inputs = list(all_test_data['test_set_2'])
# while_n_end()
print('============ End Function ============\n')

'''อ่านข้อมูลจาก input ที่มีลักษณะเป็นจำนวนเต็มเรียงกันในบรรทัดเดียว คั่นด้วยช่องว่าง 
เช่น 10 20 30 20 40 10 23
จงเขียนคำสั่งอ่านเข้ามาเก็บในลิสต์ของจำนวนเต็มชื่อ x 
เช่นจากตัวอย่างจะได้ x = [10 20 30 20 40 10 23]'''
def input_num_split():

    x = []
    n = input_test('กรอกข้อมูล: ').split()
    for i in n:
        if not i.isalpha():
            x.append(int(i))    
    print('convert:', x)

mock_inputs = list(all_test_data['test_set_3'])
# input_num_split()
print('============ End Function ============\n')

'''แบบฝึกหัด 5-3 ข้อที่ 6
อ่านข้อมูลจาก input ที่มีลักษณะเป็นรายการของรหัสภาคฯ กับชื่อภาคฯ 
ในบรรทัดเดียวกัน คั่นด้วยช่องว่าง เช่น CE Civil ME Mechanical EE 
Electrical จงเขียนคำสั่งอ่านอินพุตมาสร้างเป็นสองลิสต์ 
คือ dept_codes กับ dept_names เช่น จากตัวอย่าง จะได้ 
dept_codes = ["CE", "ME", "EE"] 
และ dept_names = ["Civil", "Mechanical", "Electrical"]'''
def dept_split_slicing():
    text = input_test('dept: ').split()
    dept_codes = text[0::2]
    dept_names = text[1::2]

    print('dept codes:', dept_codes)
    print('dept name:', dept_names)

mock_inputs = list(all_test_data['test_set_4'])
dept_split_slicing()
print('============ End Function ============\n')

