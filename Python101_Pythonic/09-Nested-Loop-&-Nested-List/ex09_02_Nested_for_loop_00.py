'''แบบฝึกหัด 9-2 ข้อที่ 1
จงเขียนโปรแกรมอ่านรายการของชื่อโรงเรียน เพื่อแสดงรายการการแข่งขันฟุตบอลแบบพบกันหมด 
โดยแสดงบรรทัดละคู่ (เรียงตามพจนานุกรม) ดูตัวอย่างในรูปประกอบ'''

def foob_ball_match_schedule(schools:str):
    teams = schools.split()
    teams.sort()

    for first in range(len(teams)):

        for last in range(first+1, len(teams)):
            
            print(teams[first], 'VS', teams[last])
foob_ball_match_schedule('BCC AC DS SK')

'''แบบฝึกหัด 9-2 ข้อที่ 2
จงเขียนโปรแกรมที่รับจำนวนเต็ม N 
เพื่อแสดงตารางสูตรคูณของแม่ 2 จนถึงแม่ N 
ดังรูป โดยขอแสดงผลการคูณด้วย 1 ถึง 5 ก็พอ 
กำหนดให้ใช้แค่ 4 ช่องเพื่อแสดงผลแต่ละจำนวน 
โดยแสดงจำนวนแบบชิดขวา (ดูรูปประกอบ) 
สามารถใช้ฟังก์ชัน left_pad ที่เขียนให้แล้ว 
และให้เขียนโปรแกรมด้วยคำสั่ง for เท่านั้น 
(ห้ามใช้ while)'''

def left_pad(n, k):
   return (' '*n + str(n))[-k:]

def multiplication_n(N:int):
    for i in range(2, N+1):
        line = ''
        for j in range(1, 5):
            line += left_pad(i*j, 4)
        print(line)

multiplication_n(12)


'''แบบฝึกหัด 9-2 ข้อที่ 3
เขียนโปรแกรมทำงานตามผังงานในรูป (แต่แทนที่จะใช้วงวน while ให้ใช้แต่ for) หมายเหตุ: อาจต้องปรับเงื่อนไขบ้างเล็กน้อย เพื่อให้เขียนในรูปของวงวน for'''
def sieve_of_eratosthenes_for_(N:int):
   
    prime = [True] * (N+1)
    prime[0] = False
    prime[1] = False

    for p in range(2, int(N**0.5) + 1):
      if prime[p]:
         for i in range(p*2, N+1, p):
            prime[i] = False
    
    return prime
result = sieve_of_eratosthenes_for_(30)
for i in range(len(result)):
   if result[i]:
      print(i, end=' ')
      
   
'''แบบฝึกหัด 9-2 ข้อที่ 4
จงเขียนฟังก์ชัน min_distance(x, y) มี x และ y เป็นลิสต์ที่เก็บพิกัด x และ y ของจุดต่าง ๆ โดยจุดที่ k มีพิกัดที่ x[k],y[k] ฟังก์ชันนี้คืนระยะทางของคู่จุดที่อยู่ใกล้กันที่สุด (ในโปรแกรมที่เขียนมีฟังก์ชัน distance มาให้ เผื่อจะใช้เป็นประโยชน์) เช่น min_distance([0, 9, 9],[0, 9, 8]) ได้ 1.0'''

def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return (dx**2 + dy**2) ** 0.5

def min_distance(x, y):
    # ตั้งให้ค่าเริ่มต้นใหญ่ ที่สุดก่อนเปรียบเทียบ
    # สูตร 1 เอาตัวรอด result = max(x) * max(y) ป๋าคิดเอง
    # สูตร 2 ค่ามากที่สุด แบบ สากล    result = float('inf')  
    # สูตร 3 เอาข้อมูลจริงมาคำนวณ result = distance(x[0],y[0],x[1],y[1]) 
    result = max(x) * max(y)
    
    for i in range(len(x)):

        for j in range(i+1, len(x)):
            min_d = distance(x[i], y[i] ,x[j], y[j])

            if min_d < result:
                result = min_d
    return result

x = [0, 9, 9]
y = [0, 9, 8]
print()
print(min_distance(x, y))



'''แบบฝึกหัด 9-2 ข้อที่ 5
จงเขียนฟังก์ชัน print_month(m, y) รับเลขเดือนและเลขปี ค.ศ. 
เพื่อจะแสดงปฏิทินของเดือนปีที่ได้รับ (รูปแสดงตัวอย่างปฏิทินของเดือนสิงหาคม 2019) 
กำหนดให้วันแรกของสัปดาห์คือวันอาทิตย์ และมีฟังก์ชัน days_in_month กับ day_of_week 
ให้ใช้ประโยชน์'''

def days_in_month(m, y):
    if m == 2:
        if y%400 or y%4==0 and y%100 != 0:
            return 29
        else:
            return 28
    elif m in [4,6,9,11]:
        return 30
    else:
        return 31
#-----------------------------------------
def day_of_week(d, m, y):
    # 0 -> Sunday, 1 -> Monday, ...
    if m < 3 :
        m += 12
        y -= 1
    c = y // 100
    k = y % 100
    w = (d+26*(m+1)//10+k+k//4+c//4+5*c)%7
    return (w-1) % 7   
#-----------------------------------------
def print_month(m, y):
    print(" SU MO TU WE TH FR SA")


