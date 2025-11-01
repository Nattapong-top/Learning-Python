# อยากทราบว่า นับจากเวลาบ่ายโมง 13:00:00 ไปอีก 98789 วินาที 
# จะเป็นเวลาอะไร ให้เขียนคำสั่งคำนวณและแสดงผล ในรูปแบบ HH:MM:SS
# คำนวณวันเวลาที่เพิ่มเข้ามาด้วย

from datetime import datetime, timedelta

# 1. ตั้งเวลาเริ่มต้น (ต้องใช้ datetime object เต็มรูปแบบ)
# ใช้ ปี เดือน วัน จำลอง 2000, 1, 1 
start_time = datetime(2000, 1, 1, 13, 0, 0)

# 2. วินาทีที่ต้องการปวก
seconds_to_add = 98789 


# 3. สร้าง object "ช่วงเวลา" (timedalta)
duration = timedelta(seconds=seconds_to_add)
end_time = start_time + duration

# 4. คำนวณช่วงวันเวลาที่เพิ่มเข้ามา
# divmod(a, b) เป็นฟังก์ชัน Pythonic ที่จะคืนค่า (ผลหาร, เศษ) ในครั้งเดียว
# divmod(seconds_to_add, 86400) จะได้ (จำนวณวัน, วินาทีที่เหลือ)
day, remaining_seconds = divmod(seconds_to_add, 24 * 60 * 60)

# divmod(reminig_seconds, 3600) จะได้เป็น (จำนวน ชั่วโมง, วินาทีที่เหลือ)
hours, remaining_seconds = divmod(remaining_seconds, 60 * 60)

# divmod(reamining_seconds, 60) จะได้ (จำนวนนาที, วินาที่สุดท้าย)
minutes, seconds = divmod(remaining_seconds, 60)

# 5. แสดงผลลัพธ์
print(f'เวลาเริ่มต้น: {start_time.strftime('%H:%M:%S')}')
print(f'บวกเพิ่ม: {seconds_to_add} วินาที')
print(f'---'*10)
print(f'คิดเป็น: {day} วัน, {hours} ขั่วโมง, {minutes} นาที, {seconds} วินาที')
print(f'---'*10)
print(f'เวลาใหม่คือ: {end_time.strftime('%H:%M:%S')}')




