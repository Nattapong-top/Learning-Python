'''แบบฝึกหัด 9-1 
ข้อที่ 1 จงเขียนโปรแกรมที่รับจำนวนเต็ม N เพื่อแสดงตารางสูตรคูณของแม่ 2 จนถึงแม่ N ดังรูป 
โดยขอแสดงผลการคูณด้วย 1 ถึง 5 ก็พอ กำหนดให้ใช้แค่ 4 ช่องเพื่อแสดงผลแต่ละจำนวน
โดยแสดงจำนวนแบบชิดขวา (ดูรูปประกอบ) สามารถใช้ฟังก์ชัน left_pad ที่เขียนให้แล้ว 
และให้เขียนวงวนในโปรแกรมด้วยคำสั่ง while เท่านั้น (ห้ามใช้ for)'''

'''
       2   4   6   8  10
       3   6   9  12  15
       4   8  12  16  20
       5  10  15  20  25
       6  12  18  24  30
'''

def left_pad(n, k):
    #แปลง n เป็นสตริงที่ยาว k โดยเติมช่องว่างทางซ้าย
    # left_pad(12, 4) ได้ "    12"
    return (' '*k + str(n))[-k:]

def mul_n():
    n = int(input('num: '))
    i = 2
    while i <= n:
        j = 1
        line = ''
        
        while j <= 5:
            line += left_pad(i*j,4)
            j += 1
        print(line)
        i += 1
mul_n()



'''ผังงาน Sieve of Eratosthenes (คัดกรองจำนวนเฉพาะ)'''

def sieve_of_eratosthenes(N):

    prime = [True] * (N+1)
    prime[0] = False
    prime[1] = False
    p = 2

    while p*p <= N:
        i = 0
        if prime[p] == True:
            i = 2*p
            while i <= N:
                prime[i] = False
                i += p
        p += 1
    return prime
print(sieve_of_eratosthenes(6))
    

