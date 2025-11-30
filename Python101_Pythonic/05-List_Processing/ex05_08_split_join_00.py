'''เขียนคำสั่งอ่านชื่อย่อธนาคารจากอินพุต แต่ละชื่อคั่นด้วยช่องว่าง 
(อาจมีมากกว่าหนึ่งช่อง) เช่น SCB BBL KBANK 
เพื่อจัดรูปแบบและแสดงให้ชื่อคั่นด้วย comma 
และช่องว่างหนึ่งช่อง เช่น SCB, BBL, KBANK
KTB    BBL  SCB KBANK    TMB'''

def banks_name_split(data:str):
    banks = data.split()
    print(', '.join(banks))

banks_name_split(data='KTB    BBL  SCB KBANK    TMB')
print('============ End Function ============\n')

'''แบบฝึกหัด 5-8 ข้อที่ 2
เขียนคำสั่งอ่านรายการของจำนวนเต็มจากอินพุต แต่ละจำนวนคั่นด้วยช่องว่าง 
มาเพิ่มค่าจำนวนละอีก 1 แล้วเก็บผลลัพธ์เป็นสตริงในตัวแปรชื่อ output 
เช่น รับ 10 20 30 จะได้ output เป็น "11 21 31
10 99 199 39 20"'''

def input_num_plus_1(data:str):
    num = map(int, data.split())
    print(data)
    print(' '.join(str(n+1) for n in num))

input_num_plus_1(data='11 21 31 10 99 199 39 20')
print('============ End Function ============\n')

'''แบบฝึกหัด 5-8 ข้อที่ 3
โปรแกรมที่ข้างล่างนี้ รับจำนวนเต็มจากอินพุต แล้วแสดงตัวประกอบทั้งหมด 
โดยแสดงบรรทัดละตัว (ลอง run ดู โดยระบบจะป้อนอินพุตให้อัตโนมัติด้วยค่า 8568) 
จงเปลี่ยนโปรแกรมนี้ให้ตัวประกอบในบรรทัดเดียวกันโดยมีตัว x คั่น เช่น 
เมื่ออินพุตเป็น 8568 จะแสดง 2x2x2x3x3x7x17'''

def print_join_x(data:str):
    num = int(data)
    print(num)

    p = []
    k = 2
    while k <= num:
        if num%k == 0:
            p.append(str(k))
            num //= k
        else:
            k += 1
    
    print('x'.join(p))

print_join_x(data='8568')
print('============ End Function ============\n')
