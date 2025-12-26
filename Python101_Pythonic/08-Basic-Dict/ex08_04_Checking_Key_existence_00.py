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



