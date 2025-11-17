'''อ่านสตริงจาก input แล้วแยกสตริงออกเป็นสองส่วน เพื่อนำไปแสดง 
โดยตัวแยกอาจเป็น @ หรือ : หรือ - หรือ + ก็ได้ เช่น abc@def 
แยกได้เป็น abc กับ def 
(สตริงที่รับมามีตัวแยกที่กำหนดไว้ตัวใดตัวหนึ่งแค่ตัวเดียวแน่ ๆ)'''
def split_text(text:str):

    for i in range(len(text)):
        if text[i] in '@:-+=':
            break
    s1 = text[:i]
    s2 = text[i+1:]
    print(s1, s2)
split_text('abc@def')

'''แบบฝึกหัดข้อที่แล้ว ประกันว่ามีตัวแยกแน่ ๆ ในสตริงที่อ่านเข้ามาจาก input 
ในข้อนี้สตริงที่อ่านมาอาจไม่มีตัวแยกก็ได้ ถ้าไม่มีก็แสดงสตริงเดิมที่รับมา 
ถ้ามีตัวแยก ก็แสดงเหมือนข้อที่แล้ว'''
def split_text2(text:str):

    clean_text = True

    for i in range(len(text)):
        if text[i] in '@:-+=':
            clean_text = False
            break
    
    if not clean_text:
        s1 = text[:i]
        s2 = text[i+1:]
        print(s1, s2)
    
    else:
        print(text)
split_text2('abc@def')
split_text2('abcdfdef')
