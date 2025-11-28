'''แบบฝึกหัด 5-5 ข้อที่ 1
กำหนดให้มีตัวแปร num เป็นลิสต์เก็บจำนวนเต็มมาให้แล้ว 
จงนับว่าใน num มีข้อมูลคู่ที่ติดกันเหมือนกันอยู่กี่คู่ 
เช่น num = [1,1,1,1,2,2] มีติดกันหมือนกันอยู่ 4 คู่'''

def most_than(num:list):

    result = sum(1 for x, y in zip(num, num[1:]) if x == y)

    print('Result:', result)

most_than(num=[1,1,1,1,2,2])
print('-'*40)
most_than(num=[1,2,1,2,1,2])
print('-'*40)

'''แบบฝึกหัด 5-5 ข้อที่ 2
กำหนดให้มีตัวแปร num เป็นลิสต์เก็บจำนวนเต็มมาให้แล้ว จงตรวจว่า ข้อมูลใน num 
จากซ้ายไปขวา เรียงค่าจากน้อยไปมากหรือไม่ ถ้าใช่แสดง YES, ไม่ใช่ แสดง NO'''

'''วิธีทีการเปรียบเทียบ แบบ pythonic เบื้องต้นมีสองแบบ 
1. แบบง่าย ใช้ sorted(x) syntax ดังนี้'''

def sort_least(x:list):

    if x == sorted(x):
        print('YES')
    else:
        print('NO')

sort_least(x=[1,1,1,1,2,2])
print('-'*40)
sort_least(x=[1,2,1,2,1,2])
print('-'*40)

'''2. แบบที่สอง ใช้ all() จะตอบ True ก็ต่อเมื่อ "ทุกเงื่อนไขข้างใน" เป็นจริงทั้งหมด'''
def is_sorted_logic(x:list):

    result = all( a <= b for a, b in zip(x, x[1:]))

    print('YES' if result else 'NO')

is_sorted_logic(x=[1,1,1,1,2,2])
print('-'*40)
is_sorted_logic(x=[1,2,1,2,1,2])
print('-'*40)