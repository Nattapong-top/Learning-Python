'''แบบฝึกหัด 7-3 ข้อที่ 1
จงเขียนฟังก์ชัน dedent(line) ที่คืนสตริงใหม่ที่มีค่าภายในเหมือน line 
แต่ลดจำนวนช่องว่างเฉพาะที่อยู่ติดกันทางซ้ายสุดลงครึ่งหนึ่ง เช่น 
dedent("        a =    0") ได้ "  a =    0"'''
# ข้อนี้ดูเฉลย งงกับโจทย์
def dedent(line:str):
    t = 0
    for i in line:
        if i != ' ':
            break
        t += 1
    return line[t//2:]

print(dedent("        a =    0"))

'''แบบฝึกหัด 7-3 ข้อที่ 2
จงเขียนฟังก์ชัน rot5_digits(s) ที่คืนสตริงใหม่ที่มีค่าภายในเหมือน s 
แต่เปลี่ยนเฉพาะตัวเลขข้างในจากเลข 0,1,2,3,4,5,6,7,8 และ 9 เป็น 5,6,7,
8,9,0,1,2,3 และ 4 ตามลำดับ เช่น rot5_digits("My number is 
02-218-6981") ได้ "My number is 57-763-1436"'''

# โค๊ดนี้ป๋าคิดเอง
def rot5_digits(s:str):
    new_s = ''
    num = '0123456789'
    for i in range(len(s)):
        if s[i].isdigit():
            idx = num.find(s[i])
            new_s += num[(idx+5) % 10]
        else:
            new_s += s[i]
    return new_s
print(rot5_digits("My number is 02-218-6981"))

# โค๊ดอาจารย์
def rot5_digits1(s):
    rot5 = ""
    for e in s:
        if "0" <= e <= "9":
            rot5 += str((int(e)+5) % 10)
        else:
            rot5 += e
    return rot5
print(rot5_digits1("My number is 02-218-6981"))

'''สตริง DNA เป็นสตริงที่มีตัวอักษรแค่ A, T, G และ C เท่านั้น 
จงเขียนฟังก์ชัน count_bases(dna) คืนลิสต์ที่เก็บจำนวนเบสที่พบใน dna 
โดยเก็บจำนวนของ A, T, G และ C ในช่องที่ 0, 1, 2, และ 3 
ตามลำดับของลิสต์ที่คืน เช่น count_bases("AAAATTTGGC") ได้ [4, 3, 2, 
1]'''
# ป่าเขียนเอง
def count_bases(dna:str):
    count_dna = [0,0,0,0]

    for e in dna:
        if e == 'A':
            count_dna[0] += 1
        elif e == 'T':
            count_dna[1] += 1
        elif e == 'G':
            count_dna[2] += 1
        elif e == 'C':
            count_dna[3] += 1
    return count_dna
print(count_bases("AAAATTTGGC"))

# โค๊ดอาจารย์
def count_bases2(dna):
    bases = 'ATGC'
    freq = [0,0,0,0]
    for e in dna:
        freq[bases.index(e)] += 1
    return freq
print(count_bases2("AAAATTTGGC"))