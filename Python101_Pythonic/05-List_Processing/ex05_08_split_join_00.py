import time

all_test_data = {
    'sj_1': ["192.168.1.1"],            # แยก IP Address เป็นส่วนๆ
    'sj_2': ["Somsak Somchai Somsri"],  # เอาชื่อมาต่อกันด้วยลูกศร " -> "
    'sj_3': ["081-123-4567"],           # ลบขีดออกจากเบอร์โทร (Split แล้ว Join ใหม่)
    'sj_4': ["Apple,Banana,Orange"]     # เปลี่ยนจากคั่นด้วย , เป็นคั่นด้วย |
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
'''แบบฝึกหัด 5-8: Split & Join
ผมเตรียมโจทย์มาให้ 4 ข้อ เพื่อปิดจบ บทที่ 5 อย่างสมบูรณ์ครับ

ข้อที่ 1: แยกชิ้นส่วน IP (Split) โจทย์: รับเลข IP Address (เช่น 192.168.1.1) 
เข้ามา จงแยกเลขแต่ละชุดออกมาเก็บใน List โดยตัดที่จุด . Hint: text.split('.')
'''

def split_ip():
    print('--- ข้อ 1: Split IP ---')
    ip_addr = input_test('IP Address: ')
    
    # เขียนโค้ดแยกชิ้นส่วน
    # parts = ...
    
    print('Parts:', parts)

mock_inputs = list(all_test_data['sj_1'])
split_ip()
print('\n')

'''ข้อที่ 2: สร้างแผนผังการส่งงาน (Join) โจทย์: มีรายชื่อคน ['Somsak', 'Somchai', 'Somsri'] จงเอามาต่อกันให้เป็น String เดียว โดยมีลูกศร -> คั่นกลาง Hint: ' -> '.join(list)
'''

'''def join_names():
    print('--- ข้อ 2: Join Names ---')
    names_str = input_test('Names: ')
    names_list = names_str.split() # ได้ลิสต์มาก่อน
    
    # เขียนโค้ดรวมร่างด้วยลูกศร
    # flow = ...
    
    print('Work Flow:', flow)

mock_inputs = list(all_test_data['sj_2'])
join_names()
print('\n')
ข้อที่ 3: ล้างเบอร์โทร (Combo Split & Join) โจทย์: รับเบอร์โทรที่มีขีด 081-123-4567 เข้ามา จงทำให้เป็นเบอร์สะอาด 0811234567 (ไม่มีขีด) เทคนิค: ใช้ split('-') เพื่อเอาก้อนตัวเลขออกมาก่อน แล้วใช้ join แบบไม่มีตัวคั่น ('') เชื่อมมันกลับเข้าไป

งูหลาม

def clean_phone():
    print('--- ข้อ 3: Clean Phone ---')
    phone_raw = input_test('Phone: ')
    
    # 1. แยกด้วยขีด
    # parts = ...
    
    # 2. รวมด้วยค่าว่าง (ติดกันเลย)
    # clean_number = ...
    
    print('Clean Number:', clean_number)

mock_inputs = list(all_test_data['sj_3'])
clean_phone()
print('\n')
ข้อที่ 4: เปลี่ยนตัวคั่น (Replace Delimiter) โจทย์: รับข้อมูลสินค้าที่คั่นด้วยคอมม่า Apple,Banana,Orange จงเปลี่ยนให้เป็นคั่นด้วยไปป์ Apple|Banana|Orange Hint: Split ด้วย , ก่อน แล้ว Join กลับด้วย |

งูหลาม

def change_delimiter():
    print('--- ข้อ 4: Change Delimiter ---')
    data = input_test('Data: ')
    
    # เขียนโค้ดแปลงร่าง
    # 1. Split ...
    # 2. Join ...
    
    print('New Format:', new_data)

mock_inputs = list(all_test_data['sj_4'])
change_delimiter()
print('\n')'''