'''แบบฝึกหัด 6-1 ข้อที่ 1
จงเขียนคำสั่งแสดงคำร้องของเพลง Happy Birthday to You 
ข้าง ๆ นี้ โดยการเรียกใช้ฟังก์ชัน sing ให้เป็นประโยชน์
Happy Birthday to You
Happy Birthday to You
Happy Birthday
Happy Birthday
Happy Birthday to You'''

def sing(msg:str, times:int):
    for k in range(times):
        print(msg)

hy = 'Happy Birthday to You'
hb = 'Happy Birthday'

sing(msg=hy,times=2)
sing(msg=hb,times=2)
sing(msg=hy,times=1)
print('============ End Function ============\n')

'''แบบฝึกหัด 6-1 ข้อที่ 2
จงเขียนคำสั่งในฟังก์ชัน HBD(name) ให้แสดงคำร้องอวยพรวันเกิดระบุชื่อคนด้วย 
ดังตัวอย่างข้าง ๆ นี้ (สีแดงคือชื่อคน) ภายใน HDB ต้องเรียกใช้ฟังก์ชัน 
sing ให้เป็นประโยชน์ โดยในโปรแกรมข้างล่างนี้มีฟังก์ชัน sing 
และมีคำสั่งรับชื่อ แล้วเรียก HBD ให้แสดงคำร้องอวยพรวันเกิดให้แล้ว
Happy Birthday to You
Happy Birthday to You
Happy Birthday Dear name
Happy Birthday to You
'''

hbn = 'Happy Birthday Dear '

def HBD(name:str):
    sing(msg=hy, times=2)
    sing(msg=hbn + name, times=1)
    sing(msg=hy, times=1)

HBD(name='Top')
print('============ End Function ============\n')

