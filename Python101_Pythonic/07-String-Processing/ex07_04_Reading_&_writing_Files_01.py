import os  # เรียกใช้ไลบรารี os (เอาไว้สั่งงาน Windows สร้างโฟลเดอร์/ลบไฟล์)

# ตั้งชื่อโฟลเดอร์ที่จะเก็บงาน
folder_name = "my_files"

# ---------------------------------------------------------
# ขั้นตอนที่ 1: เตรียมพื้นที่ (สร้างโฟลเดอร์)
# ---------------------------------------------------------
# os.makedirs = สั่งสร้างโฟลเดอร์
# exist_ok=True = ถ้ามีโฟลเดอร์นี้อยู่แล้ว ก็ไม่ต้อง Error (ใช้ของเดิมได้เลย)
os.makedirs(folder_name, exist_ok=True)

print(f"✅ ตรวจสอบโฟลเดอร์ '{folder_name}' เรียบร้อยครับ\n")


# ---------------------------------------------------------
# ขั้นตอนที่ 2: สร้างไฟล์ตัวอย่าง (เอาไว้ทดสอบ)
# ---------------------------------------------------------
# การใช้ f"{folder_name}/..." คือการระบุว่าให้ไฟล์ไปอยู่ในโฟลเดอร์นั้น

# สร้างไฟล์ที่ 1: เก็บรายชื่อผลไม้
with open(f'{folder_name}/data1.txt', 'w') as f:
    f.write("Apple\nBanana\nOrange\nMango") # \n คือขึ้นบรรทัดใหม่

# สร้างไฟล์ที่ 2: เก็บรายชื่อสัตว์
with open(f'{folder_name}/data2.txt', 'w') as f:
    f.write("Cat\nDog\nBird")

# สร้างไฟล์ที่ 3: บทความภาษาอังกฤษ (เอาไว้นับ a, an, the)
with open(f'{folder_name}/article.txt', 'w') as f:
    f.write("This is a book.\nThat is an apple.\nThe sun is hot.")

print("✅ สร้างไฟล์จำลองเสร็จแล้ว พร้อมรันโปรแกรม!\n")


# ---------------------------------------------------------
# ขั้นตอนที่ 3: ฟังก์ชันใช้งานจริง (ตามโจทย์)
# ---------------------------------------------------------

'''
ข้อ 1: ฟังก์ชันนับจำนวนบรรทัด
- รับค่า: file_path (ที่อยู่ไฟล์)
- คืนค่า: จำนวนบรรทัด (int)
'''
def count_line(file_path):
    print(f"--- 1. กำลังนับบรรทัดไฟล์: {file_path} ---")
    
    # ใช้ try...except เพื่อกันโปรแกรมพัง ถ้าหาไฟล์ไม่เจอ
    try:
        fn = open(file_path) # เปิดสมุด (ไฟล์)
        c = 0                # ตัวนับ เริ่มที่ 0
        
        # วนลูปอ่านทีละบรรทัด (จนกว่าจะหมดสมุด)
        for line in fn:
            c += 1           # เจอ 1 บรรทัด ให้นับเพิ่ม 1
            
        fn.close()           # ปิดสมุด (สำคัญมาก! ต้องคืนทรัพยากรให้เครื่อง)
        return c             # ส่งผลยอดรวมกลับไป
        
    except FileNotFoundError:
        print(f"❌ โอ๊ะ! หาไฟล์ไม่เจอครับป๋า: {file_path}")
        return 0


'''
ข้อ 2: ฟังก์ชันอ่านไฟล์สลับฟันปลา (Merge)
- รับค่า: path1, path2 (ที่อยู่ไฟล์ทั้งสอง)
- การทำงาน: อ่านบรรทัดแรกของไฟล์ 1, แล้วอ่านไฟล์ 2, สลับไปเรื่อยๆ
'''
def print_merge(path1, path2):
    print(f"--- 2. กำลัง Merge ไฟล์: {path1} กับ {path2} ---")
    try:
        f1 = open(path1) # เปิดไฟล์ซ้าย
        f2 = open(path2) # เปิดไฟล์ขวา
        
        # อ่านบรรทัดแรกมารอก่อนเลย (เตรียมตัว)
        d1 = f1.readline()
        d2 = f2.readline()
        
        # ลูป while: ทำไปเรื่อยๆ ตราบใดที่ "ไฟล์ 1 ยังเหลือ" หรือ "ไฟล์ 2 ยังเหลือ"
        # (len > 0 แปลว่ายังมีตัวหนังสือให้อ่านอยู่)
        while (len(d1) > 0 or len(d2) > 0):
            
            # ถ้าไฟล์ 1 ยังเหลือ -> ปริ้นท์ -> อ่านบรรทัดต่อไปมารอ
            if len(d1) > 0:
                print(f"ไฟล์ 1: {d1.strip()}") # strip() เพื่อลบ \n ทิ้ง จะได้ไม่เว้นบรรทัดห่าง
                d1 = f1.readline() # หยิบของชิ้นต่อไปมารอ
                
            # ถ้าไฟล์ 2 ยังเหลือ -> ปริ้นท์ -> อ่านบรรทัดต่อไปมารอ
            if len(d2) > 0:
                print(f"ไฟล์ 2: {d2.strip()}")
                d2 = f2.readline() # หยิบของชิ้นต่อไปมารอ
                
        # ปิดไฟล์ทั้งคู่
        f1.close()
        f2.close()
        
    except FileNotFoundError:
        print("❌ หาไฟล์ไม่เจอครับ เช็คชื่อไฟล์ดีๆ นะครับ")


'''
ข้อ 3: ฟังก์ชันนับคำนำหน้า (a, an, the)
ประกอบด้วย 3 ฟังก์ชันย่อยช่วยกันทำงาน
'''

# 3.1 ฟังก์ชันช่วยล้างขยะ (เครื่องหมายวรรคตอน)
def replace_punctuation(s):
    t = ""
    # วนลูปเช็คตัวอักษรทีละตัว
    for e in s:
        # ถ้าเป็นพวกเครื่องหมายแปลกๆ (เช่น " ' . ,)
        if e in "\"\'/\\,.:;()[]{}":
            t += " "   # เปลี่ยนเป็นช่องว่าง
        else:
            t += e     # ถ้าเป็นตัวหนังสือปกติ ก็เก็บไว้เหมือนเดิม
    return t

# 3.2 ฟังก์ชันช่วยนับคำ
def count_word(words_list, target_word):
    target_word = target_word.lower() # แปลงคำที่จะหาเป็นตัวเล็ก (จะได้ไม่พลาด)
    count = 0
    # วนลูปดูคำในลิสต์ทีละคำ
    for e in words_list:
        if e.lower() == target_word: # เจอคำที่เหมือนกันเป๊ะๆ
            count += 1
    return count
    
# 3.3 ฟังก์ชันหลัก (พระเอกของข้อนี้)
def count_articles(file_path):
    print(f"--- 3. กำลังนับคำในไฟล์: {file_path} ---")
    try:
        fn = open(file_path)
        total_count = 0 # ตัวนับรวมผลลัพธ์
        
        for line in fn: # อ่านทีละบรรทัด
            # Step 1: ล้างเครื่องหมายวรรคตอนทิ้ง
            clean_line = replace_punctuation(line)
            
            # Step 2: หั่นประโยคให้เป็นคำๆ (List of words)
            words = clean_line.split()
            
            # Step 3: ส่งไปนับทีละคำ แล้วบวกสะสมยอด
            total_count += count_word(words, "a")
            total_count += count_word(words, "an")
            total_count += count_word(words, "the")
            
        fn.close()
        return total_count
        
    except FileNotFoundError:
        print(f"❌ หาไฟล์ไม่เจอครับ: {file_path}")
        return 0


# ---------------------------------------------------------
# ขั้นตอนที่ 4: เริ่มทดสอบการทำงาน
# ---------------------------------------------------------

# กำหนดตัวแปรเก็บที่อยู่ไฟล์ (Path) ให้ชัดเจน
path_file_1 = f"{folder_name}/data1.txt"  # my_files/data1.txt
path_file_2 = f"{folder_name}/data2.txt"  # my_files/data2.txt
path_article = f"{folder_name}/article.txt" # my_files/article.txt

# --- เริ่มรันข้อ 1 ---
lines_count = count_line(path_file_1)
print(f">> ผลลัพธ์: มีทั้งหมด {lines_count} บรรทัด\n")

# --- เริ่มรันข้อ 2 ---
print_merge(path_file_1, path_file_2)
print("\n")

# --- เริ่มรันข้อ 3 ---
total_articles = count_articles(path_article)
print(f">> ผลลัพธ์: เจอ a, an, the ทั้งหมด {total_articles} คำ")