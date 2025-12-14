'''ข้อที่ 1: นักกวี (Quotes & Newlines)
โจทย์: จงเขียนคำสั่ง print เพียงบรรทัดเดียว 
เพื่อให้แสดงผลข้อความออกมาหน้าตาแบบนี้เป๊ะๆ 
(มีฟันหนูและขึ้นบรรทัดใหม่):'''

print("เขากล่าวว่า \"Python\" เขียนง่าย\n\tแต่ต้อง 'ระวัง' เรื่อง Indent")

# ข้อที่ 2: เส้นทางวินโดวส์ (Windows Path Splitting)
# โจทย์: รับข้อความที่เก็บ Path ของไฟล์ใน Windows ซึ่งใช้เครื่องหมาย \ 
# (Backslash) คั่น เช่น path = r"C:\Users\Admin\Documents\Work.txt" 
# จงแยก (Split) ให้ออกมาเป็น List: ['C:', 'Users', 'Admin', 
# 'Documents', 'Work.txt

path = r"C:\Users\Admin\Documents\Work.txt"

list_path = path.split('\\')
print(list_path)


'''ข้อที่ 3: ล้างบางบรรทัดใหม่ (Clean Newlines)
โจทย์: มีข้อความยาวๆ ที่ก็อปปี้มาจาก PDF ซึ่งมันชอบมี \n 
(ขึ้นบรรทัดใหม่) แทรกอยู่กลางประโยคมั่วไปหมด จงลบ \n 
ออกให้หมดแล้วแทนที่ด้วยช่องว่าง เพื่อให้เป็นประโยคยาวๆ บรรทัดเดียว 
text = "This is a long\nsentence that was\nbroken into lines."'''

text = "This is a long\nsentence that was\nbroken into lines."

new_text = text.replace('\n', ' ')
print(new_text)

'''ข้อที่ 4: สร้างตารางด้วย Tab (Tab Formatting)
โจทย์: จงใช้ f-string ร่วมกับ \t (Tab) เพื่อสร้างตาราง 2 
คอลัมน์ง่ายๆ ให้พิมพ์ออกมาดังนี้:'''
print(f'id\tname')
print(f'101\tSomchai')
print(f'102\tSomsak')

'''ข้อที่ 5: ป้องกัน SQL Injection (Sanitize Input)
โจทย์: (ข้อนี้ใช้งานจริงบ่อยมาก) สมมติรับข้อมูลชื่อมาจาก User แต่ 
User ตัวดีดันพิมพ์เครื่องหมาย ' (Single Quote) เข้ามา ซึ่งอาจทำให้ 
Database พังได้ จงเขียนฟังก์ชันที่เปลี่ยน ' ทุกตัว ให้กลายเป็น \' 
(Escape มันซะ) เช่นรับ John's -> ต้องได้ John\'s'''


name = "John's"
name = name.replace("'","\\'")
print(name)
