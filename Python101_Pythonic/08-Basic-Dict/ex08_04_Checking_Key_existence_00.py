'''แบบฝึกหัด 8-4 ข้อที่ 1
p1 และ p2 เป็นดิกเก็บคะแนนของนักเรียนที่เรียนวิชา 1 และ 2 
ตามลำดับในรูปแบบ {เลขประจำตัว: คะแนน} จงเขียนฟังก์ชัน take_both(st_id, p1, p2) 
เพื่อหาว่านักเรียนที่มีเลขประจำตัว st_id เรียนทั้งสองวิชาหรือไม่'''

def take_both(st_id, p1, p2):
    if st_id in p1 and st_id in p2:
        return True
    else:
        return False



'''แบบฝึกหัด 8-4 ข้อที่ 2
p1 และ p2 เป็นดิกเก็บคะแนนของนักเรียนที่เรียนวิชา 1 และ 2 
ตามลำดับในรูปแบบ {เลขประจำตัว: คะแนน} จงเขียนฟังก์ชัน both(p1, p2) 
เพื่อคืนลิสต์ที่เก็บเลขประจำตัวนักเรียนเรียนทั้งสองวิชา 
โดยเรียงลำดับเลขประจำตัวนักเรียนในลิสต์จากน้อยไปมากด้วย'''

def both(p1:list, p2:list):
    result = []

    for sid in p1:
        if sid in p2:
            result.append(sid)
    
    result.sort()
    return result


'''แบบฝึกหัด 8-4 ข้อที่ 3
สตริง DNA เป็นสตริงที่มีตัวอักษรแค่ A, T, G และ C เท่านั้น จงเขียนฟังก์ชัน count_bases(dna) คืนดิกในรูปแบบ {เบส: จำนวน} เช่น count_bases("AAAATTTGG") ได้ {"A":4, "T":3, "G":2, "C":0}'''

def count_bases(dna):
    a = 'ATGC'
    c = {}
    for e in a:
        c[e] = 0
    
    for d in dna:
        if d in c:
            c[d] += 1
    
    return c

print(count_bases("AAAATTTGG"))


'''แบบฝึกหัด 8-4 ข้อที่ 4
จงเขียนฟังก์ชัน count_chars(text) ที่นับว่าใน text มีอักขระอะไรเท่าไรบ้าง 
(โดยให้ตัวอักษรเล็กเหมือนใหญ่ เช่น count_chars("ABCabcZ") ได้ดิก 
{'A': 2, 'B': 2, 'C': 2, 'Z': 1} เป็นผลลัพธ์'''

def count_chars(text:str):
    chars = {}
    
    for c in text.upper():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars



'''แบบฝึกหัด 8-4 ข้อที่ 5
income1 และ income2 เป็นดิกในรูปแบบ {รหัสสาขาร้าน: รายได้} 
ซึ่งเก็บรายรับของร้านอาหารสาขาต่าง ๆ จงเขียนฟังก์ชัน merge(income1, income2) 
ที่คืนดิกใหม่ในรูปแบบเดียวกัน แต่เก็บข้อมูลรวมจากทั้งสองดิกที่รับมา เช่น 
income1 = {"P100":100, "P200":200} และ income2 = {"P200":300, "P300":90} 
merge กันแล้วจะได้ดิกใหม่ {"P100":100, "P200":500, "P300":90}'''

def merge(income1:dict, income2:dict):
    merge_income = income1.copy()

    for item in income2:
        if item in income2:
            merge_income[item] += income2[item]
        else:
            merge_income[item] = income2[item]
    
    return merge_income

'''แบบฝึกหัด 8-4 ข้อที่ 6
จงเขียนโปรแกรมอ่านบรรทัดแรกของอินพุตเป็นรายการของรหัสสินค้า 
บรรทัดที่สองเป็นรายการของราคา (มีจำนวนข้อมูลเท่ากับของบรรทัดแรก 
โดยสินค้าชิ้นที่ตำแหน่ง i ก็มีราคาที่ตำแหน่ง i) และอ่านบรรทัดถัด ๆ มา (จบด้วย end) 
ที่เป็นรหัสสินค้าที่ต้องการให้แสดงราคา ถ้าหาไม่พบให้แสดง Not found 
จากตัวอย่างจะแสดง 35.0, Not found และ 50.0 บรรทัดละราคา (หรือข้อความ)'''

def input_end():
    # 1. รับรหัสสินค้า และ ราคา (แค่ 2 บรรทัดแรก) 
    pids = input('รหัสสินค้า: ').strip().split()
    prices = input('ราคา: ').strip().split()

    # 2. สร้าง Dict (ใช้ท่าไม้ตาย zip ของป๋า)
    # zip(pids, prices) จะจับคู่ รหัส-ราคา ให้เอง แล้วแปลงเป็น dict เลย
    products = dict(zip(pids, prices))

    # 3. เริ่มช่วงถาม-ตอบ (Query Loop)
    while True:
        check = input('เช็คราคาด้วยรหัสสินค้า: ').strip()
        if check == 'end':
            break
    
        if check in products:
            print(products[check])
        else:
            print('Not Found')

input_end()

        


