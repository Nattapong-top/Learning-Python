'''แบบฝึกหัด 9-3 ข้อที่ 1
ฟังก์ชัน count_digit(x, d) รับ x เป็นลิสต์ของจำนวนเต็ม และ d 
เป็นจำนวนเต็มที่เก็บเลขโดด 0 ถึง 9 ตัวใดตัวหนึ่ง ฟังก์ชันนี้คืนจำนวนเลขโดดใน 
d ที่ปรากฎในจำนวนเต์มทั้งหมดของ x (เช่น x = [333, 23, 4], d = 3 นับแล้วจะคืน 
4 เพราะมี 3 อยู่ 4 ตัวใน x) จงแยกวงวน while ออกเป็นฟังก์ชัน 
และปรับให้เรียกใช้ฟังก์ชันใหม่ เพื่อให้ทำงานได้เหมือนเดิม 
แต่ไม่มีวงวนซ้อนกัน'''

def count(n:int, d:int):
    c = 0
    while n > 0:
        if n%10 == d:
            c += 1
        n //= 10
    return c

def count_digit(x:list, d:int):
    c = 0
    for n in x:
        c += count(n, d)
    return c
x = [333, 23, 4]; d = 3
print(count_digit(x, d))


'''แบบฝึกหัด 9-3 ข้อที่ 2
จงเขียนฟังก์ชัน longest_suffix(words) รับ words เป็นลิสต์ของสตริง 
ฟังก์ชันนี้คืน สตริงที่ยาวสุดที่ปรากฏเป็นส่วนท้ายของทุกสตริงใน words เช่น 
longest_suffix(["programming", "scramming", "Diagramming"]) ได้ "ramming"'''

# version ด้นสด 
def longest_suffix(words:list):
    print(words)
    base = words[0][::-1]

    for i in range(1,len(words)):
        re_words = words[i][::-1]
        len_min = min(len(base), len(re_words))
        suffix = ''
        for ch in range(len_min):
            if base[ch] == re_words[ch]:
                suffix += base[ch]
            else:
                break
        base = suffix
    return suffix[::-1]
words = ["programming", "scramming", "Diagramming"]
print(longest_suffix(words))


'''แบบฝึกหัด 9-3 ข้อที่ 3
ฟังก์ชัน reverse_and_add(n) คืนผลบวกของ n กับเลขที่เขียนกลับลำดับของ n เช่น 96+69 ได้ 165 ถ้าเราเริ่มที่จำนวนเต็มค่าหนึ่ง แล้วทำ reverse_and_add ไปเรื่อย ๆ มักจะจบทีจำนวนเต็มที่เป็นพาลินโดรม เช่น 96 -> 96+69 = 165 -> 165+561 = 726 -> 726+627 = 1353 -> 1353+3531 = 4884 เป็นพาลินโดรม แต่ก็มีจำนวนเต็มบางจำนวนที่ทำแบบนี้แล้วไม่เป็น เช่น 196 เราเรียกจำนวนแบบนี้ว่า Lychrel number

จงเขียนโปรแกรมรับจำนวนเต็ม N แล้วแสดง Lychrel number ที่มีค่าน้อยที่สุดที่มากกว่า N กำหนดให้ การสรุปว่าเป็น Lychrel number คือเมื่อทำ reverse_and_add ไปแล้ว 30 รอบ ก็ยังไม่ใช่พาลินโดรม (ต้องขอบอกว่า ข้อกำหนดนี้ไม่เป็นความจริงนะ เพียงต้องการให้เขียนโปรแกรมง่ายเท่านั้น)'''