'''
รับจำนวนจริง a , b และ e จาก input (ในบรรทัดเดียวกัน คั่นด้วยช่องว่าง) แล้วแสดงคำว่า close enough ถ้า 
|a−b|≤e⋅max(|a|,|b|)
เป็นจริง ไม่เช่นนั้น แสดงว่า not equal
'''
def bisection1():
    a, b, e = map(float, input('ป้อนตัวเลข (แบ่งตัวช่วงว่าง): ').strip().split(' '))

    if abs(a - b) <= e * max(abs(a), abs(b)):
        print('Close Enough')
    else:
        print('Not Equal')
# bisection1()



'''
รับจำนวนจริง x จาก input แล้วใช้วิธี bisection หาและแสดงค่าของ 3√x (รากที่ 3 ของ x)กำหนดให้ a และ b  มีค่าเกือบเท่ากัน 
เมื่อ |a−b|≤10−6max(|a|,|b|)'''

def bisection2():
    x = float(input('ป้อนตัวเลข: '))
    l = 0; u = x
    r = (l + u) / 2
    r3 = pow(r, 3)

    while abs(r3 - x) > 1e-6 * max(r3, x):
        if r3 > x:
            u = r
        else:
            l = r
        
        r = (l + u) / 2
        r3 = pow(r, 3)

    print(r)
# bisection2()
        
