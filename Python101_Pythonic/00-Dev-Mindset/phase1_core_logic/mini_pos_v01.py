# --- โปรแกรม POS ร้านชานม V0.1 ---

import os
from datetime import datetime


# 1. ข้อมูล (Data)
menu = {
    "ชานม": 40,
    "ชาเขียว": 50,
    "ชาไทย": 45
}


def get_datetime():
    # ดึงเวลาปัจจุบัน
    now = datetime.now()
    # จัดรูปแบบให้อ่านง่ายๆ (วัน/เดือน/ปี ชั่วโมง:นาที:วินาที)
    timestamp = now.strftime('%d/%m/%y %H:%M:%S')

    return timestamp


def get_quantity()->int:
    while True:
        quantity_str = input("รับกี่แก้วครับ: ")
        if quantity_str.isdigit() and int(quantity_str) > 0:
            return int(quantity_str)
        print('ใส่ตัวเลขจำนวนเต็ม และต้องมากกว่า 0 ครับ')


def get_price_order(order:str,quantity:int) -> int:
    # 3. คำนวณ (Process)
    price = menu[order]      # ดึงราคา
    total = price * quantity # คูณจำนวน
    return total


def show_summary(order, quantity, total, change):
    # 4. แสดงผล (Output)
    print("-" * 20) # ขีดเส้นกั้นสวยๆ
    print(f'--- {get_datetime()} ---')
    print(f"คุณสั่ง {order} จำนวน {quantity} แก้ว")
    print(f"เงินทอน {'-'if change == 0 else change} บาท")
    print(f"ราคารวมทั้งหมด {total} บาท")
    print("-" * 20)


def save_sales_log(order, quantity, total):
    try:
        timestamp = get_datetime()
        # --- ส่วน GPS หาที่อยู่ไฟล์ ---
        script_path = os.path.abspath(__file__) 
        current_folder = os.path.dirname(script_path)
        file_path = os.path.join(current_folder, 'sales_log.txt')
        # ---------------------------
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'{timestamp} เมนู: {order}, จำนวน: {quantity}, ราคา: {total} บาท\n')
    except Exception as e:
        print(f'เกิดข้อผิดพลาด! บันทึกไฟล์ไม่ได้: {e}')


def get_culcalate_money(total:int):
    while True:
        print(f'ยอดเงินรวม {total} บาท')
        money_str = input('ชำระเงิน: ')
        if money_str.isdigit():
            money = int(money_str)
            if money >= total:
                change = money - total
                print(f'💰 รับเงิน {money} บาท, เงินทอน {change}')
                return change
            else:
                print(f'ยอดเงินไม่พอ ขาดอีก {total - money} บาท')
        else:
            print('ใส่เป็นตัวเลขเท่านั้นครับ')

def main_menu():
        
    total_quantity = 0
    grand_total = 0
    
    while True:
        # 2. รับออเดอร์ (Input)
        print("รายการเมนู:", menu) # โชว์เมนูให้ลูกค้าดูก่อน
        order = input("รับเมนูอะไรดีครับ: ")
        if order in menu:
            quantity = get_quantity()
            total = get_price_order(order, quantity)
            total_quantity += quantity
            grand_total += total     # ยอดเงินรวม
            change = get_culcalate_money(total)
            show_summary(order, quantity, total, change)
            save_sales_log(order, quantity, total)


        elif order.upper() == 'END':
            print('--- โปรแกรม POS ร้านชานม ---')
            print(f'--- {get_datetime()} ---')
            print(f'--- ยอดขายรวมวันนี้ {grand_total} บาท จำนวน {total_quantity} แก้ว  ---')
            break

        else:
            print(f'{order} ไม่มีในรายการครับ')
main_menu()