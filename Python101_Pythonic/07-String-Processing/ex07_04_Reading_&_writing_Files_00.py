'''แบบฝึกหัด 7-4 ข้อที่ 1
จงเขียนฟังก์ชัน count_line(file_name) เพือหาจำนวนบรรทัดของข้อมูลในแฟ้มชื่อ file_name'''

def count_line(file_name:str):
    fn = open(file_name)
    c = 0
    for line in fn:
        c += 1
    fn.close
    return c


'''แบบฝึกหัด 7-4 ข้อที่ 2
จงเขียนฟังก์ชัน print_merge(filename1, filename2) 
อ่านข้อมูลของแต่ละบรรทัดจากทั้งสองแฟ้มมาสลับกันแสดงทางจอภาพ (เริ่มที่ 
file_name1) ถ้าแฟ้มใดหมด ก็อ่านอีกแฟ้มมาแสดงให้หมด'''

def print_merge(filename1, filename2):
    f1 = open(filename1)
    f2 = open(filename2)
    d1 = f1.readline()
    d2 = f2.readline()
    while (len(d1) > 0 or len(d2) > 0):
        if len(d1) > 0:
            print(d1.strip())
            d1 = f1.readline()
        if len(d2) > 0:
            print(d2.strip())
            d2 = f2.readline()
    f1.close()
    f2.close()

    
'''แบบฝึกหัด 7-4 ข้อที่ 3
จงเขียนฟังก์ชัน count_articles(filename) อ่านข้อความจากแฟ้มชื่อ filename 
เพื่อนับว่าในแฟ้มนี้มีคำว่า a, an และ the รวมทั้งหมดทุกบรรทัดในแฟ้มกี่ตัว'''

def replace_punctuation(s):
    t = ""
    for e in s:
        if e in "\"\'/\\,.:;()[]{}":
            t += " "
        else:
            t += e
    return t

def count_word(words, w):
    w = w.lower()
    c = 0
    for e in words:
        if e.lower() == w:
            c += 1
    return c
    
def count_articles(filename):
    # นับจำนวน a, an และ the ของคำในแฟ้ม filename
    fn = open(filename)
    c = 0
    for line in fn:
        words = replace_punctuation(line).split()
        c += count_word(words, "a")
        c += count_word(words, "an")
        c += count_word(words, "the")
    fn.close()
    return c