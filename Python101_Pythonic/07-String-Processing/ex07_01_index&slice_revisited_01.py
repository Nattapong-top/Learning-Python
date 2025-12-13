import time

'''ชุดข้อมูลทดสอบ'''
all_test_data = {
    'str_1': ["   Latte   "],           # ตัดช่องว่าง
    'str_2': ["Espresso"],              # เช็คว่ามี s กี่ตัว
    'str_3': ["Green Tea"],             # หาคำว่า "Tea" อยู่ index ไหน
    'str_4': ["Cappuccino 50 Baht"],    # เปลี่ยน Baht เป็น THB
    'str_5': ["mOcHa"]                  # ทำให้เป็นชื่อสวยๆ (ตัวแรกใหญ่ ที่เหลือเล็ก)
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

'''ข้อที่ 1: ทำความสะอาด (Strip)
โจทย์: รับชื่อเมนูที่มีช่องว่างเกินๆ มา จงตัดช่องว่างหน้าหลังออกให้หมด'''
def clean_menu():
    print('--- ข้อ 1 ---')
    menu = input_test('Menu: ')
    
    clean = menu.strip()
    
    print(f"Clean: '{clean}'") # ใส่ '' ครอบเพื่อให้เห็นว่าช่องว่างหายจริง

mock_inputs = list(all_test_data['str_1'])
clean_menu()
print('\n')


'''ข้อที่ 2: นับจำนวน (Count)
โจทย์: รับชื่อเมนูมา จงนับว่ามีตัวอักษร 's' (ตัวเล็ก) ผสมอยู่กี่ตัว'''
def count_char():
    print('--- ข้อ 2 ---')
    menu = input_test('Menu: ')
    
    count = menu.count('s')
    
    print(f"Found 's': {count} ตัว")

mock_inputs = list(all_test_data['str_2'])
count_char()
print('\n')


'''ข้อที่ 3: ตามหาตำแหน่ง (Find)
โจทย์: จงหาว่าคำว่า "Tea" เริ่มต้นที่ Index ที่เท่าไร
(ถ้าหาไม่เจอ มันจะคืนค่า -1)'''
def find_tea():
    print('--- ข้อ 3 ---')
    menu = input_test('Menu: ')
    
    idx = menu.find('Tea')
    
    print(f"'Tea' at index: {idx}")

mock_inputs = list(all_test_data['str_3'])
find_tea()
print('\n')


'''ข้อที่ 4: เปลี่ยนสกุลเงิน (Replace)
โจทย์: เปลี่ยนคำว่า "Baht" ให้เป็น "THB"'''
def change_currency():
    print('--- ข้อ 4 ---')
    text = input_test('Text: ')
    
    new_text = text.replace('Baht', 'THB')
    
    print(f"New: {new_text}")

mock_inputs = list(all_test_data['str_4'])
change_currency()
print('\n')


'''ข้อที่ 5: จัดระเบียบชื่อ (Capitalize)
โจทย์: รับชื่อที่พิมพ์มามั่วๆ (เช่น mOcHa) จงเปลี่ยนให้
"ตัวแรกเป็นตัวใหญ่ ตัวที่เหลือเป็นตัวเล็ก" (Mocha)
Hint: ใช้ .capitalize() หรือผสม .upper() + .lower() เองก็ได้'''
def fix_name():
    print('--- ข้อ 5 ---')
    name = input_test('Name: ')
    
    fixed = name.lower().capitalize()
    
    print(f"Fixed: {fixed}")

mock_inputs = list(all_test_data['str_5'])
fix_name()
print('\n')



'''ชุดข้อมูลทดสอบ'''
product = "Latte"
price = 50
vat = 3.5
total = 53.5

'''ข้อที่ 1: จัดทศนิยม (Decimal)
โจทย์: จงแสดงค่า VAT ให้เหลือทศนิยม 2 ตำแหน่ง
Hint: f"VAT: {vat:...}"'''
def format_vat():
    # เขียนโค้ดตรงนี้
    print(f'{vat:.2f}')
    
# เรียกใช้
print('--- ข้อ 1 ---')
format_vat() # ต้องได้ 3.50


'''ข้อที่ 2: ใส่ลูกน้ำ (Comma)
โจทย์: สมมติยอดขายเยอะมาก จงแสดงเลข 1234567.89 ให้มีลูกน้ำคั่น
Hint: f"ยอดขาย: {sales:...}"'''
def format_sales():
    sales = 1234567.89
    # เขียนโค้ดตรงนี้
    print(f'{sales:,.2f}')

print('\n--- ข้อ 2 ---')
format_sales() # ต้องได้ 1,234,567.89


'''ข้อที่ 3: จัดหน้าใบเสร็จ (Alignment) - ข้อสอบจริง!
โจทย์: จงจัดหน้าให้ ชื่อสินค้าชิดซ้าย และ ราคาชิดขวา (ในความกว้าง 20 ตัวอักษร)
Latte                50
Hint: f"{ชื่อ:<20} {ราคา}"'''
def print_receipt():
    item = "Cappuccino"
    cost = 55
    # เขียนโค้ดตรงนี้
    print(f'{item:<10}{cost:>11}')
    print(item.ljust(10), str(cost).rjust(10))
    print(f'{item:<10}{cost:>11}')

print('\n--- ข้อ 3 ---')
print_receipt() 
# ผลลัพธ์ที่อยากได้ (กะด้วยสายตา):
# Cappuccino            55