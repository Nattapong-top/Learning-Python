'''แบบฝึกหัด 6-4: Modifying List Parameter (Hard Mode)
ข้อที่ 1: ผลรวมสะสม (Running Sum) จงเขียนฟังก์ชัน running_sum(x)
หน้าที่: เปลี่ยนค่าใน x ให้แต่ละช่องเก็บ "ผลรวมตั้งแต่ตัวแรกจนถึงตัวมันเอง"'''

def running_sum(x):
    # เขียนโค้ดตรงนี้
    for i in range(1, len(x)):
        x[i] = (x[i]+x[i-1])

x = [1, 2, 3, 4]
running_sum(x)
print('sum:', x)


'''ข้อที่ 2: เซ็นเซอร์คำหยาบ (Censor List) 
จงเขียนฟังก์ชัน censor(text_list, bad_word)
หน้าที่: ตรวจสอบทุกคำใน text_list ถ้าคำไหน "มี" 
คำว่า bad_word ผสมอยู่ ให้เปลี่ยนคำนั้นเป็นดอกจัน * ตามจำนวนตัวอักษรของคำนั้น
ตัวอย่าง:
msg = ["hello", "damn", "world", "goddamn"]
เรียก censor(msg, "damn")
msg เปลี่ยนเป็น ["hello", "****", "world", "*******"]'''

def censor(text_list, bad_word):
    # เขียนโค้ดตรงนี้
    t = 0
    for i in range(len(text_list)):
        if bad_word in text_list[i]:
            text_list[i] = '*' * len(text_list[i])

msg = ["hello", "damn", "world", "goddamn"]
censor(msg, 'damn')
print(msg)

'''ข้อที่ 3: หมุนวงล้อ (Rotate Left) จงเขียนฟังก์ชัน rotate_left(x)
หน้าที่: ย้ายข้อมูลตัวแรกสุด ไปต่อท้ายแถว (เลื่อนทุกคนมาข้างหน้า 1 ขั้น)
ตัวอย่าง:
data = [10, 20, 30, 40]
เรียก rotate_left(data)
data เปลี่ยนเป็น [20, 30, 40, 10]
'''

def rotate_left(x:list):
    # เขียนโค้ดตรงนี้
    j = x.pop(0)
    x.append(j)

data = [10, 20, 30, 40]
rotate_left(data)
print(data)

'''ข้อที่ 4: กลับด้านเฉพาะช่วง (Partial Reverse) จงเขียนฟังก์ชัน reverse_part(x, start, end)
หน้าที่: กลับด้านข้อมูลใน x เฉพาะช่วง Index ตั้งแต่ start ถึง end (รวมตัวจบ) ส่วนที่เหลือห้ามแตะต้อง
ตัวอย่าง:
nums = [0, 1, 2, 3, 4, 5, 6]
เรียก reverse_part(nums, 2, 4) (กลับด้าน index 2 ถึง 4 คือเลข 2, 3, 4)
nums เปลี่ยนเป็น [0, 1, 4, 3, 2, 5, 6]
'''

def reverse_part(x:list, start, end):
    # เขียนโค้ดตรงนี้
    x[start:end+1] = x[start:end+1][::-1]

nums = [0, 1, 2, 3, 4, 5, 6]
reverse_part(nums, 2, 4)
print(nums)

'''ข้อที่ 5: ลบตัวปัญหา (Remove All - The Trap!) จงเขียนฟังก์ชัน remove_all(x, val)
หน้าที่: ลบข้อมูลใน x ทุกตัวที่มีค่าเท่ากับ val
ข้อควรระวัง: ระวังเรื่อง Index เลื่อนเวลาลบของ (ข้อนี้ปราบเซียนครับ ถ้าวนลูปไม่ดี จะลบไม่หมด)
ตัวอย่าง:
data = [1, 5, 5, 2, 5]
เรียก remove_all(data, 5)
data เปลี่ยนเป็น [1, 2]
'''

def remove_all(x, val):
    # เขียนโค้ดตรงนี้
    for i in range(len(x)-1, -1, -1):
        if x[i] == val:
            x.pop(i)

data = [1, 5, 5, 2, 5]
remove_all(data, 5)
print(data)