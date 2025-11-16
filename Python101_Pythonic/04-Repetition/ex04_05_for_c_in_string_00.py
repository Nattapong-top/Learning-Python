'''
โจทย์ for c in string จากเว็บจุุฬา 
'''
# ให้นับตัวอักษรทุกตัวที่รับเข้ามา ว่ามีตัวเลขกี่ตัว
def check_digit(digit:str):

    # สร้างตัวแปร นับจำนวนตัวเลข
    count_digit = 0

    # ลูปตัวอักษร ทุกตัว 
    for c in digit:

        # เช็ตตัวอักษรว่าเป็น ตัวเลขหรือไม่
        if c.isdigit():
            # ถ้าเป็นตัวเลข นับเพิ่ม 1
            count_digit += 1
    
    print(digit, 'ตัวเลข =',count_digit, 'ตัว')
    print('-' * 20)

check_digit(digit='abc012def789')

'''ให้ตรวจสอบตัวอักษรทุกตัวที่รับเข้ามา ว่ามีสัญลักษณ์พิเศษหรือไม่
ถ้ามีให้เปลี่ยนเป็น เว้นวรรค แทน'''
def check_symbol(input_str:str ='P(ython), J(ava).'):
    alpha = ''

    for ch in input_str:

        if not ch.isalnum():
            alpha += ' '
        else:
            alpha += ch
    
    print(input_str, 'คัดเฉพาะตัวอักษร =', alpha)
    print('-' * 20)

check_symbol()


'''อ่านสตริงจาก input จากนั้นแสดงเฉพาะตัวอักษรอังกฤษในสตริงที่อ่านมาจากซ้ายไปขวา 
บรรทัดละตัว เช่น อ่านมาเป็น "A-B-123 &" จะแสดงแค่ A กับ B 
(บรรทัดละตัว)'''
def check_alpha(alpha:str = 'A-B-123 &'):

    print(alpha)

    for ch in alpha:
        if ch.isalpha():
            print(ch)

    print('-' * 20)
    
check_alpha()

'''อ่านสตริงจาก input หนึ่งบรรทัด 
จากนั้นแสดงเฉพาะตัวอักขระในสตริงที่อยู่ที่ index คี่ (ตัวซ้ายสุดคือ 
index 0) บรรทัดละตัว เช่น อ่านมาเป็น "*ABCDE*" 
จะแสดงแค่ A, C กับ E (บรรทัดละตัว)'''
def check_index_str(input_str:str = "*ABCDE*"):

    print(input_str)

    for ch in input_str[1::2]:
        print(ch)

    print('-' * 20)

check_index_str()

'''อ่านสตริงหนึ่งบรรทัดจาก input 
แล้วแสดงตัวอักษรในสตริงที่อ่านมาจากขวามาซ้าย ABCDabcd บรรทัดละตัว'''
def check_str_reversed(input_str:str = 'ABCDabcd'):

    print(input_str)
    for ch in input_str[::-1]:
        print(ch)

    print('-' * 20)
check_str_reversed()