'''------------------------------------------
ชุดข้อมูลตั้งต้น (สำหรับทุกข้อ)
------------------------------------------'''
# พจนานุกรมเก็บคะแนนสอบของนักเรียน
scores = {
    'Somchai': 75,
    'Somsak': 80,
    'Somsri': 90
}

'''ข้อที่ 1: แก้คะแนนและเพิ่มคนใหม่ (Add & Update)
โจทย์: 
1. นาย Somchai ไปขอแก้คะแนน จงเปลี่ยนคะแนน Somchai เป็น 78
2. มีเด็กใหม่ชื่อ "Mana" เข้ามา ได้คะแนน 85 จงเพิ่มเข้าไปใน dict
Hint: ใช้ d[key] = value
'''
def update_scores():
    # ก๊อปปี้มาเพื่อไม่ให้กระทบข้ออื่น
    current_scores = scores.copy() 
    
    # 1. แก้คะแนน Somchai
    current_scores['Somchai'] = 78

    # 2. เพิ่ม Mana
    current_scores['Mana'] = 85

    print(f"ข้อ 1: {current_scores}")

update_scores()
print('\n')


'''ข้อที่ 2: ไล่ออก (Delete)
โจทย์: 
นาย Somsak ลาออก จงลบชื่อและคะแนนของ Somsak ออกจาก dict
Hint: ใช้คำสั่ง del ...
'''
def remove_student():
    current_scores = scores.copy()
    
    # เขียนโค้ดลบตรงนี้
    del current_scores['Somsak']
    
    print(f"ข้อ 2: {current_scores}")

remove_student()
print('\n')


'''ข้อที่ 3: นับคะแนนโหวต (Frequency Count) - **ท่าหากิน!**
โจทย์: มีรายการโหวตใน List จงนับคะแนนแล้วเก็บใส่ Dict
- ถ้ายังไม่มีชื่อใน Dict ให้สร้างใหม่แล้วใส่ค่า 1
- ถ้ามีชื่อแล้ว ให้บวกค่าเพิ่มอีก 1
'''
def count_votes(votes_list):
    vote_result = {} # Dict เปล่า
    
    for name in votes_list:
        if name in vote_result:
            # มีชื่อแล้ว บวกเพิ่ม
            vote_result[name] += 1
        else:
            # ยังไม่มีชื่อ สร้างใหม่
            vote_result[name] = 1
            
    return vote_result

votes = ['A', 'B', 'A', 'A', 'C', 'B']
print(f"ข้อ 3: {count_votes(votes)}")
# ผลลัพธ์ควรได้: {'A': 3, 'B': 2, 'C': 1}
print('\n')


'''ข้อที่ 4: ปรับราคาขึ้น (Batch Update)
โจทย์: มี Dict ราคาสินค้า จงวนลูปปรับราคา "ทุกชิ้น" ให้แพงขึ้น 10%
Hint: ต้องใช้ for k in ... เพื่อดึง key มาทีละตัว แล้วค่อยแก้ค่า
'''
def increase_price():
    prices = {'Coffee': 50, 'Tea': 40, 'Water': 10}
    
    # วนลูป key ของ prices
    for k in prices:
        # แก้ค่าของ prices[k] ให้เป็นราคาใหม่ (คูณ 1.1) -> แปลงเป็น int ด้วยก็ดี
        prices[k] = int(prices[k] * 1.1)
    print(f"ข้อ 4: {prices}")

increase_price()
print('\n')


'''ข้อที่ 5: พจนานุกรมแปลคำศัพท์ (Dict from Input)
โจทย์: รับข้อความที่คั่นด้วยลูกน้ำ เช่น "apple=แอปเปิ้ล,banana=กล้วย"
จงตัดคำและเอาไปใส่ใน Dict ให้ใช้งานได้จริง
Hint: 
1. split(',') เพื่อแยกคู่
2. split('=') เพื่อแยก key กับ value
3. เก็บใส่ dict
'''
def create_vocab_dict(text):
    vocab = {}
    
    # เขียนโค้ดแปลงร่าง text เป็น dict
    parts = text.split(',')
    for frut in parts:
        en, th = frut.split('=')
        vocab[en] = th

    return vocab

raw_text = "apple=แอปเปิ้ล,banana=กล้วย,cat=แมว"
my_dict = create_vocab_dict(raw_text)
print(f"ข้อ 5: {my_dict}")
print(f"ลองแปล apple: {my_dict.get('apple')}") # ต้องได้ 'แอปเปิ้ล'