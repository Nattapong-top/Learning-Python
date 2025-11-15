'''
มีรายการของจำนวนเต็มในบรรทัดเดียวกันของ input เช่น 10 20 30 55 
จงเขียนชุดคำสั่งอ่านจำนวนเต็มเหล่านี้เก็บใส่ตัวแปรชื่อ a ที่เป็นลิสต์ 
จากนั้นสร้างลิสต์ของจำนวนจริงมีขนาดเท่ากับของ a 
แต่ละช่องเก็บค่าครึ่งหนึ่งของที่เก็บใน a เช่น อ่านข้อมูลได้ 
a = [10,20,30,55] แล้วก็สร้าง b = [5.0, 10.0, 15.0, 27.5]
'''
def ex04_04_for_convier_to_list():
    a = ['10','20','30','55']

    b = [float(i)/2 for i in a]

    print(b)

# ex04_04_for_convier_to_list()

'''
อ่านจำนวนเต็ม n จาก input แล้วแสดงรูปสามเหลี่ยมดังตัวอย่างข้าง ๆ นี้
'''
def ex04_04_10():
    n = int(input())

    for i in range(n+1):
        print('*'*i)
# ex04_04_10()

'''
อ่านจำนวนเต็ม n จาก input แล้วแสดงรูปสามเหลี่ยมดังตัวอย่างข้าง ๆ นี้
'''
def ex04_04_11():
    n = 5#int(input())
    for i in range(1, n+1):
        print('*'*i)
    for i in range(n-1, 0, -1):
        print('*'*i)
ex04_04_11()

'''
อ่านจำนวนเต็ม n จาก input แล้วแสดงรูปสามเหลี่ยมดังตัวอย่างข้าง ๆ นี้
'''
def ex04_04_12():
    n = int(input())

    for i in range(1, n+1):
        print(' '*(n-i) + '*'*i)
# ex04_04_12()

'''
อ่านสตริง t จาก input เพื่อนับและแสดงว่ามีสระใน t กี่ตัว 
(นับทั้งตัวเล็กและตัวใหญ่ โดยใช้วงวน for) เช่น Anna มีสระเป็นจำนวน 2 
ตัว แบบฝึกหัดของบทก่อน เราเขียนโดยใช้วงวน while ดังแสดงข้างล่างนี้
'''
def ex04_04_13():
    t = 'NATEIPOUG'#input()
    c = 0
    vowels = 'aeiou'
    for i in vowels:
        if i.lower() in vowels:
            c += 1
    print(f'ตัวอักษร: {t}, vowels: {c}, count: {t}')
# ex04_04_13()

'''
อ่านสตริง t จาก input แล้วนับและแสดงว่ามีสตริงย่อย "ABC" 
อยู่ภายในกี่ตำแหน่ง เช่น "ABCabcAABCABAABC" มี "ABC" อยู่ 3 ตำแหน่ง
'''
def ex04_04_14():
    t = 'ABcABCxAxBABC'#input()
    count = 0
    pattern = 'ABC'
    for i in range(len(t)):
        # check ตัวอักษรทุกตัว ตัวแรกถึงตัวสุดท้าย
        if t[i:].startswith(pattern):
            count += 1
    print(count)
# ex04_04_14()

'''
อ่านสตริง t จาก input มาหนึ่งบรรทัด แล้วก็อ่านสตริง s จาก input 
อีกหนึ่งบรรทัด จากนั้นนับและแสดงว่า มีสตริงของ s อยู่ภายในสตริงของ t 
กี่ตำแหน่ง เช่น t = "ABCabcAABCABAABC" และ s = "ABC" จะแสดง 3
'''
def ex04_04_15():
    t = input('input1: ') #'ABCabcAABCABAABC'
    s = input('input2: ' ) #'ABC'
    count = 0
    for i in range(len(t)):
        if t[i:].startswith(s):
            count += 1
            print(f'print I: {i}')
    print(count)
ex04_04_15()


