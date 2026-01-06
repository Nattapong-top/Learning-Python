# --- โปรแกรม POS ร้านชานม V0.1 ---

import os


# 1. ข้อมูล (Data)
menu = {
    "ชานม": 40,
    "ชาเขียว": 50,
    "ชาไทย": 45
}

total_quantity = 0
grand_total = 0

def get_quantity()->int:
    while True:
        quantity_str = input("รับกี่แก้วครับ: ")
        if quantity_str.isdigit():
            break
        print('ใส่ตัวเลขเท่านั้นครับ')
    return int(quantity_str)

def get_price_order(order:str,quantity:int) -> int:
    # 3. คำนวณ (Process)
    price = menu[order]      # ดึงราคา
    total = price * quantity # คูณจำนวน
    return total

def show_summary(order, quantity, total):
    # 4. แสดงผล (Output)
    print("-" * 20) # ขีดเส้นกั้นสวยๆ
    print(f"คุณสั่ง {order} จำนวน {quantity} แก้ว")
    print(f"ราคารวมทั้งหมด {total} บาท")
    print("-" * 20)

def save_sales_log(order, quantity, total):
    try:
        # --- ส่วน GPS หาที่อยู่ไฟล์ ---
        script_path = os.path.abspath(__file__) 
        current_folder = os.path.dirname(script_path)
        file_path = os.path.join(current_folder, 'sales_log.txt')
        # ---------------------------
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'เมนู: {order}, จำนวน: {quantity}, ราคา: {total} บาท\n')
    except Exception as e:
        print(f'เกิดข้อผิดพลาด! บันทึกไฟล์ไม่ได้: {e}')
while True:
    # 2. รับออเดอร์ (Input)
    print("รายการเมนู:", menu) # โชว์เมนูให้ลูกค้าดูก่อน
    order = input("รับเมนูอะไรดีครับ: ")
    if order in menu:
        quantity = get_quantity()
        total = get_price_order(order, quantity)
        total_quantity += quantity
        grand_total += total     # ยอดเงินรวม
        show_summary(order, quantity, total)
        save_sales_log(order, quantity, total)


    elif order.upper() == 'END':
        print('--- โปรแกรม POS ร้านชานม ---')
        print(f'--- ยอดขายรวมวันนี้ {grand_total} บาท จำนวน {total_quantity} แก้ว  ---')
        break

    else:
        print(f'{order} ไม่มีในรายการครับ')