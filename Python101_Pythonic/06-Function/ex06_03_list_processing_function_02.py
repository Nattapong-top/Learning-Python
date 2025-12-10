'''ข้อที่ 1: คนในความลับ (Local Scope)
โจทย์: ลองรันโค้ดดูครับ ว่าทำไมมัน Error? 
และต้องแก้ยังไงให้ print ค่า x ออกมาได้?
(Hint: ตัวแปร x เกิดในฟังก์ชัน ก็ตายในฟังก์ชัน)'''

def create_secret():
    # global x ไม่ค่อยแนะนำให้ใข้วิธีนี้ ถ้าโปรแกรมใหญ่ขึ้นจะมีปัญหาในอนาตค
    x = 999
    print(f"ในฟังก์ชันเห็น x: {x}")
    return x

x = create_secret()
print(f"นอกฟังก์ชันเห็น x: {x}") # <--- บรรทัดนี้ Error! จงคอมเมนต์บรรทัดนี้ทิ้ง หรือแก้วิธีรับค่า


'''ข้อที่ 2: ชื่อเหมือนแต่คนละคน (Shadowing)
โจทย์: มีตัวแปร a ข้างนอก และ a ข้างใน
จงทายผลลัพธ์ว่า บรรทัด print จะแสดงเลขอะไรบ้าง?'''

a = 10 # Global

def change_a():
    a = 50 # Local (คนละตัวกับข้างนอก)
    print(f"1. ในฟังก์ชัน a คือ: {a}")

change_a()
print(f"2. นอกฟังก์ชัน a คือ: {a}") # ป๋าคิดว่าเป็น 10 หรือ 50?

# a global 10 a local 50

'''ข้อที่ 3: กับดัก List เปลี่ยนค่า (Side Effect) - เรื่องซีเรียส!
โจทย์: เราแค่อยากจะ "ทดลอง" เพิ่มข้อมูลใน List แต่ไม่อยากให้ของจริงเปลี่ยน
จงแก้ฟังก์ชันนี้ ให้ "ไม่กระทบ" กับ List ต้นฉบับ
Hint: ใช้ .copy() หรือ สร้าง list ใหม่'''

def try_add(items):
    new_items = items.copy() #... (สร้างตัวใหม่แทน)
    new_items.append('TEST') # <--- แบบนี้ของจริงพัง! จงแก้บรรทัดนี้
    return new_items #(ส่งตัวใหม่กลับไป)

real_data = ['A', 'B', 'C']
result = try_add(real_data)
print(f"ของจริงต้องเหมือนเดิม: {real_data}") # ต้องได้ ['A', 'B', 'C'] เท่าเดิม
print(f"ของก๊อปต้องเปลี่ยนไป: {result}") # ต้องได้ ['A', 'B', 'C'] เท่าเดิม



'''ข้อที่ 4: อ่านได้แต่เขียนไม่ได้ (Global Read-Only)
โจทย์: โค้ดนี้ Error เพราะพยายามแก้ค่า score (ที่เป็น Global) โดยไม่มีใบอนุญาต
จงแก้ให้ถูกต้อง โดยการรับ score เข้ามาเป็น parameter แล้ว return ค่าใหม่ออกไป'''

score = 0

def add_score(score):
    score += 10 # <--- Error! (UnboundLocalError)
    return score

score = add_score(score) # แก้เป็นแบบนี้แทน
print(f"Score ใหม่: {score}")


'''ข้อที่ 5: ค่าเริ่มต้นมหาภัย (Mutable Default Argument)
โจทย์: โค้ดนี้เป็น Bug ในตำนานของ Python!
ถ้าเรากำหนด default list = [] ในพารามิเตอร์ มันจะใช้ list ก้อนเดิมซ้ำๆ!
จงแก้ให้เป็น item_list=None แล้วเช็คข้างในแทน'''

def add_item(item, item_list=None): # <--- ห้ามทำแบบนี้!
    # ข้อควรระวัง ควรเช็ค list ก่อนว่า list ที่ส่งเข้ามาเป็น list ที่มีข้อมูลอยู่
    # หรือ list ว่าง เพื่อจะได้ไม่เขียนทับข้อมูลเก่า
    if item_list is None:
        item_list = []

    item_list.append(item)
    return item_list

# # ลองรันดูจะเห็นความสยอง
# print(add_item('Apple', []))  # ['Apple']
# print(add_item('Banana', [])) # มันจะได้ ['Apple', 'Banana'] เฉยเลย! (ทั้งที่ควรได้แค่ Banana)

print(add_item('Apple'))  # ['Apple']
print(add_item('Banana')) # มันจะได้ ['Apple', 'Banana'] เฉยเลย! (ทั้งที่ควรได้แค่ Banana)
fulit2 = add_item('Apple') # มันจะได้ ['Apple', 'Banana'] เฉยเลย! (ทั้งที่ควรได้แค่ Banana)
fulit = add_item('Banana', fulit2) # มันจะได้ ['Apple', 'Banana'] เฉยเลย! (ทั้งที่ควรได้แค่ Banana)
print(fulit) # มันจะได้ ['Apple', 'Banana'] เฉยเลย! (ทั้งที่ควรได้แค่ Banana)
