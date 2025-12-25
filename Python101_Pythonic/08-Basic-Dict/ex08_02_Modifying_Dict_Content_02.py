'''------------------------------------------
ข้อที่ 1: ตัดสต็อกสินค้า (Inventory Management)
โจทย์: มีสต็อกสินค้าใน Dict และมีรายการสั่งซื้อใน List (cart)
จงวนลูปตัดสต็อกตามรายการที่สั่ง
- ถ้ามีของ: ลดจำนวนลง 1 และพิมพ์ "ขาย {item}"
- ถ้าของหมด (เป็น 0): พิมพ์ "{item} หมด!"
- ถ้าไม่มีชื่อสินค้าในสต็อก: พิมพ์ "ไม่มี {item} ในร้าน"
'''
def update_stock():
    stock = {'Espresso': 5, 'Latte': 2, 'Tea': 10}
    cart = ['Espresso', 'Latte', 'Latte', 'Latte', 'Mocha', 'Espresso']
    
    print("--- ข้อ 1: ตัดสต็อก ---")
    for item in cart:
        # เขียน Logic ตรงนี้
        # 1. เช็คว่า item อยู่ใน stock ไหม?
        if item in stock:
        # 2. ถ้าอยู่ เช็คว่าจำนวน > 0 ไหม?
            if stock[item] > 0:
        #    - ถ้ามีของ -> ลดค่า stock[item] ลง 1
                stock[item] -= 1
        #    - ถ้าไม่มี -> บอกว่าหมด
            else:
                print(f'{item} หมดแล้วครับ')
        else:
            print(f'{item} ไม่มีในร้านครับ')
        # 3. ถ้าไม่อยู่ -> บอกไม่มีในร้าน

    print(f"สต็อกคงเหลือ: {stock}")
    print('\n')


'''------------------------------------------
ข้อที่ 2: รวมบิล 2 โต๊ะ (Merge Dictionaries)
โจทย์: มีรายการขายจากโต๊ะ 1 และโต๊ะ 2
จงรวมรายการทั้งหมดเข้าด้วยกัน (Sum) เก็บใน total_bill
- ถ้าสินค้านั้นมีในทั้ง 2 โต๊ะ ต้องเอาจำนวนมาบวกกัน
- ถ้ามีแค่โต๊ะใดโต๊ะหนึ่ง ก็ใส่ค่านั้นได้เลย
'''
def merge_bills():
    table1 = {'Cake': 2, 'Coffee': 1}
    table2 = {'Cake': 1, 'Tea': 3, 'Coffee': 2}
    
    total_bill = table1.copy() # เริ่มต้นด้วยข้อมูลโต๊ะ 1 ก่อน
    
    print("--- ข้อ 2: รวมบิล ---")
    # วนลูปดูของใน table2
    for item in table2:
        # ถ้า item นี้มีใน total_bill อยู่แล้ว -> บวกเพิ่ม
        if item in total_bill:
            total_bill[item] += table2[item]
        # ถ้ายังไม่มี -> สร้างใหม่เท่ากับค่าของ table2
        else:
            total_bill[item] = table2[item]

        
    print(f"รวมยอดขาย: {total_bill}") 
    # ผลลัพธ์ควรได้ {'Cake': 3, 'Coffee': 3, 'Tea': 3}
    print('\n')


'''------------------------------------------
ข้อที่ 3: จัดหมวดหมู่สินค้า (Grouping) **ข้อปราบเซียน**
โจทย์: มีรายชื่อสินค้าพร้อมหมวดหมู่ใน List (ทูเพิล)
จงแปลงให้เป็น Dict ที่แยกหมวดหมู่ชัดเจน
Input: [('Espresso', 'Coffee'), ('GreenTea', 'Tea'), ('Latte', 'Coffee')]
Output: { 'Coffee': ['Espresso', 'Latte'], 'Tea': ['GreenTea'] }
'''
def group_menu():
    menu_list = [
        ('Espresso', 'Coffee'),
        ('GreenTea', 'Tea'),
        ('Latte', 'Coffee'),
        ('Water', 'Drink'),
        ('Coke', 'Drink')
    ]
    
    menu_dict = {}
    
    print("--- ข้อ 3: จัดหมวดหมู่ ---")
    for name, category in menu_list:
        # เช็คว่าหมวดหมู่ (category) นี้ เคยสร้างใน dict หรือยัง?
        if category in menu_dict:
        # ถ้ายัง -> สร้าง list ว่างให้มันก่อน menu_dict[category] = []
            # แล้วค่อย append ชื่อสินค้า (name) ใส่ลงไป
            menu_dict[category].append(name)
        else:
            menu_dict[category] = []
            menu_dict[category].append(name)
        
    print(f"เมนูแยกหมวด: {menu_dict}")
    print('\n')


'''------------------------------------------
ข้อที่ 4: พนักงานดีเด่น (Find Max Value)
โจทย์: หาชื่อพนักงานที่ทำยอดขายได้ "สูงสุด"
Hint: วนลูปเทียบค่าไปเรื่อยๆ (เหมือนหา King of the hill)
'''
def find_top_sales():
    sales = {'Somchai': 5000, 'Somsak': 3000, 'Somsri': 8500, 'Mana': 6000}
    
    top_name = ""
    max_amount = -1
    
    print("--- ข้อ 4: พนักงานดีเด่น ---")
    # วนลูป key และ value (ใช้ .items() จะง่ายครับ)
    for name, amount in sales.items():
        # ถ้า amount มากกว่า max_amount
        if amount > max_amount:
            # ให้จดชื่อ และ จดจำนวนใหม่ไว้
            top_name = name
            max_amount = amount
        
    print(f"คนเก่งสุดคือ: {top_name} (ยอด {max_amount})")
    print('\n')


'''------------------------------------------
ข้อที่ 5: ปรับราคาและกรองของถูก (Map & Filter)
โจทย์: สร้าง Dict ใหม่ (new_prices) โดยมีเงื่อนไข:
1. สินค้าที่ราคาเกิน 100 บาท ให้ลดราคา 10% (คูณ 0.9)
2. สินค้าที่ราคาต่ำกว่า 20 บาท **ไม่เอา** (ตัดทิ้ง)
'''
def adjust_prices():
    prices = {'Steak': 250, 'Salad': 80, 'Soup': 15, 'Pasta': 150}
    new_prices = {}
    
    print("--- ข้อ 5: ปรับราคา ---")
    for item in prices:
        price = prices[item]
        
        # เขียนเงื่อนไข
        # ถ้าราคา < 20: ข้าม (continue)
        if price < 20:
            continue
        # ถ้าราคา > 100: คำนวณใหม่ แล้วเก็บใส่ new_prices
        elif price > 100:
            new_prices[item] = price * 0.9
        # ถ้าปกติ: เก็บราคาเดิมใส่ new_prices
        else:
            new_prices[item] = price
        pass
        
    print(f"ราคาใหม่: {new_prices}")
    # Steak ควรเหลือ 225.0, Pasta เหลือ 135.0, Soup หายไป
    print('\n')

# --- เรียกใช้งาน ---
update_stock()
merge_bills()
group_menu()
find_top_sales()
adjust_prices()