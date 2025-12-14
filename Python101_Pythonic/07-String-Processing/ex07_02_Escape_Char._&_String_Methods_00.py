'''แบบฝึกหัด 7-2 ข้อที่ 1
จงเขียนฟังก์ชัน number_of_newlines(s) 
หาว่ามีรหัสขึ้นบรรทัดใหม่ในสตริง s กี่ตัว'''

def number_of_newlines(s):
    c = 0
    for e in s:
        if e == '\n':
            c += 1
    return c
s = '\n \n \n \n \n \n\n\n\n'
print(number_of_newlines(s))   

'''แบบฝึกหัด 7-2 ข้อที่ 2
จงเขียนฟังก์ชัน left_strip(s) คืนสตริงใหม่ที่เหมือน s 
แต่ไม่มีช่องว่างทางซ้าย เช่น left_strip(" ab ") ได้ "ab "'''

def left_strip(s):
    return ((s+'.').strip())[:-1]

print(left_strip(" ab "))

'''แบบฝึกหัด 7-2 ข้อที่ 3
จงเขียนฟังก์ชัน right_strip(s) คืนสตริงใหม่ที่เหมือน s 
แต่ไม่มีช่องว่างทางขวา เช่น right_strip(" ab ") ได้ " ab"'''
def right_strip(s:str):
    return (('.'+s).strip())[1:]

print(right_strip(" ab "))



'''แบบฝึกหัด 7-2 ข้อที่ 4
จงเขียนฟังก์ชัน first_index_of(s,t) หาว่ามี t ปรากฎเริ่มต้นใน s 
ที่อินเด็กซ์ใด ถ้ามีหลายที่ให้คืนอินเด็กซ์น้อยสุด ถ้าไม่มีให้คืน -1 
เช่น first_index_of("abracadabra", "bra") ได้ 1 ในขณะที่ 
first_index_of("abracadabra", "BRA") ได้ -1'''

def first_index_of(s,t):
    return s.find(t)

print(first_index_of("abracadabra", "bra"))
print(first_index_of("abracadabra", "BRA"))


'''แบบฝึกหัด 7-2 ข้อที่ 5
จงเขียนฟังก์ชัน first_index_of(s,t) หาว่ามี t ปรากฎเริ่มต้นใน s 
ที่อินเด็กซ์ใด ถ้ามีหลายที่ให้คืนอินเด็กซ์น้อยสุด ถ้าไม่มีให้คืน -1 
โดยการหาในถือว่าตัวอังกฤษเล็กเหมือนใหญ่ เช่น first_index_of
("abracadabra", "bra") ได้ 1 และ 
first_index_of("abracadabra", "BRA") ก็ได้ 1'''

def first_index_of(s:str,t:str):
    return s.lower().find(t.lower())

print(first_index_of("abracadabra", "bra"))
print(first_index_of("abracadabra", "BRA"))

'''แบบฝึกหัด 7-2 ข้อที่ 6
จงเขียนฟังก์ชัน last_index_of(s,t) หาว่ามี t ปรากฎเริ่มต้นใน s 
ที่อินเด็กซ์ใด ถ้ามีหลายที่ให้คืนอินเด็กซ์มากสุด ถ้าไม่มีให้คืน -1 
โดยการหาในถือว่าตัวอังกฤษเล็กเหมือนใหญ่ เช่น last_index_of
("abracadabra", "bra") ได้ 8 และ 
last_index_of("abracadabra", "BRA") ก็ได้ 8'''

# โค๊ด อาจารย์ กลับด้านข้อความ หาเสร็จสลับคือ แล้วนำมาคำนวณ หาจุด index
#0123456789
#-ABC---ABC ABC  7
#CBA---CBA- CBA  0  10 - 0 - 3
def last_index_of(s,t):
    k = s[::-1].lower().find(t[::-1].lower())
    if k != -1:
        k = len(s) - len(t) - k
    return k

last_index_of("abracadabra", "BRA")

# สูตรที่ป๋าคิด
def last_index_of2(s:str,t:str):
    s = s.lower() ; t = t.lower()
    current_pos = 0 ; ans = -1
    while True:
        index = s.find(t, current_pos)    
        if index == -1:
            break
        ans = index
        current_pos = index + 1      
    return ans
    
print(last_index_of2("abracadabra", "bra"))
print(last_index_of2("abracadabra", "BRA"))

# แบบ pythonic pythonic
def last_index_of_pro(s, t):
    # .rfind() = Right Find (หาจากขวามาซ้าย = หาตัวที่มี index มากสุด)
    return s.lower().rfind(t.lower())

print(last_index_of_pro("abracadabra", "bra")) # ได้ 8 เท่ากันเป๊ะ



'''แบบฝึกหัด 7-2 ข้อที่ 7
จงเขียนฟังก์ชัน index_of_kth(s,t,k) คืนอินเดกซ์ของสตริง s ที่ปรากฏสตริง t เป็นครั้งที่ k ถ้าไม่พบคืน -1 เช่น index_of_kth("ABabAB", "AB", 1) ได้ 0, index_of_kth("ABabAB", "AB", 2) ได้ 4, index_of_kth("ABabAB", "AB", 3) ได้ -1'''

def index_of_kth(s:str, t:str, k:int):
    j = -1               # 1. จุดเริ่มต้น (ตั้งไว้นอกสนาม)
    for i in range(k):   # 2. วนลูป "ตามจำนวนครั้งที่ต้องการ" (k รอบ)
        j = s.find(t, j+1) # 3. หาทีละขยัก (เริ่มหาต่อจากจุดเดิม)
        
        if j == -1:      # 4. ถ้าหาไม่เจอระหว่างทาง
            return -1    #    เลิกคุย! กลับบ้านเลย
            
    return j             # 5. ถ้าจบลูปครบ k รอบ ส่งตำแหน่งล่าสุดคืนไป

print(index_of_kth("ABCabc--ABC-AABC-", "AB", 5))
print( index_of_kth("ABabAB", "AB", 3))


'''แบบฝึกหัด 7-2 ข้อที่ 8
จงเขียนฟังก์ชัน remove_duplicates(s) ที่รับสตริง s 
แล้วคืนสตริงใหม่ที่เหมือน s แต่ไม่มีตัวอักษรที่ซ้ำครั้งแรกเป็นต้นไป 
โดยตัวอังกฤษใหญ่เหมือนตัวอังกฤษเล็ก เช่น remove_duplicates
("AbaaaaBbBbC") จะได้ "AbC"'''

def remove_duplicates(s):
    result = ''
    seen = ''
    for c in s:
        if c.lower() not in seen:
            result += c
            seen += c.lower()
    return result

print(remove_duplicates("AbaaaaBbBbC"))



'''แบบฝึกหัด 7-2 ข้อที่ 9
จงเขียนฟังก์ชัน contains(s, w) เพื่อตรวจว่ามี w ที่ปรากฎเป็น "คำ" 
ในสตริง s หรือไม่ ให้ถือว่าอักขระที่คั่นระหว่างคำมีดังนี้ " ' / 
\ , . : ; ( ) [ ] { } กับช่องว่าง 
และถือว่าตัวอังกฤษใหญ่เหมือนกับเล็ก ดังนั้น contains("That's all 
folks", "that") จะได้ผลเป็นจริง แต่ contains("That's all folks", 
"folk") ได้ผลเป็นเท็จ'''

# โค๊ดอาจารย์
def replace(s, symbols, c):
    t = ""
    for e in s:
        if e in symbols:
            t += " "
        else:
            t += e
    return t

def contains(s, w):
    t = " " + replace(s.lower(), "\"\'/\\,.:;()[]{}", " ") + " "
    return t.find(" " + w.lower() + " ") != -1
print(contains("That's all folks", "that"))
print(contains("That's all folks","folk"))


# โค๊ดป๋า 
def contains2(s:str, w:str):
    s = s.lower() ; w = w.lower()
    delimiters = '''" ' / \ , . : ; ( ) [ ] { }'''
    new_s = ''
    for c in s:
        if c in delimiters:
            new_s += c.replace(c,' ')
        else:
            new_s += c
    list_s = new_s.split()
    return w in list_s

print(contains2("That's all folks", "that"))
print(contains2("That's all folks","folk"))


