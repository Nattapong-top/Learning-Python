import os

folder_name = "my_files"
os.makedirs(folder_name, exist_ok=True)

# 1. ไฟล์ log การทำงาน (สำหรับโจทย์ข้อ 1)
with open(f'{folder_name}/server_log.txt', 'w') as f:
    f.write("INFO: System started\n")
    f.write("WARNING: High memory usage\n")
    f.write("ERROR: Database connection failed\n")
    f.write("INFO: User logged in\n")
    f.write("ERROR: Timeout waiting for response\n")

# 2. ไฟล์ยอดขาย (สำหรับโจทย์ข้อ 2)
with open(f'{folder_name}/sales.txt', 'w') as f:
    f.write("Coffee,50\n")
    f.write("Tea,30\n")
    f.write("Cake,120\n")
    f.write("Water,10")

# 3. ไฟล์คะแนนนักเรียน (สำหรับโจทย์ข้อ 4)
with open(f'{folder_name}/scores.txt', 'w') as f:
    f.write("Somchai 85\n")
    f.write("Somsak 92\n")
    f.write("Somsri 78\n")
    f.write("Mana 95")

# 4. ไฟล์รหัสผ่าน (สำหรับโจทย์ข้อ 5)
with open(f'{folder_name}/users.db', 'w') as f:
    f.write("admin:1234\n")
    f.write("paa:password\n")
    f.write("guest:guest")

print(f"✅ สร้างไฟล์โจทย์ในโฟลเดอร์ {folder_name} เรียบร้อย!")

'''
📝 โจทย์ 5 ข้อ (File I/O)
ข้อที่ 1: นักสืบ Error (Filter Lines)

โจทย์: จงเขียนฟังก์ชัน find_errors(filename) อ่านไฟล์ Log แล้วพิมพ์เฉพาะบรรทัดที่มีคำว่า "ERROR" ออกมา

Hint: if "ERROR" in line:
'''
def find_errors(file_name):
    print('โปรแกรมค้นหา ERROR')

    try:
        fn = open(file_name)
        for line in fn:
            if 'ERROR' in line:
                print(line, end='')
        fn.close()
    except FileNotFoundError:
        print(f"❌ โอ๊ะ! หาไฟล์ไม่เจอครับป๋า: {file_name}")
find_errors(f'{folder_name}/server_log.txt')


'''
ข้อที่ 2: เครื่องคิดเลขร้านค้า (Sum CSV)

โจทย์: จงเขียนฟังก์ชัน calc_total(filename) อ่านไฟล์ยอดขาย (Format: สินค้า,ราคา) แล้วคืนค่า ผลรวมราคา ทั้งหมด

Hint: line.split(',') แล้วเอาตัวหลังมา int() (ระวัง \n ต้อง .strip() ก่อน)'''
def calc_total(file_name:str):
    try:
        fn = open(file_name)
        sum = 0
        for line in fn:
            prod, price = line.strip('\n').split(',')
            sum += int(price)
        fn.close()
        return sum
    except FileNotFoundError:
        print(f"❌ โอ๊ะ! หาไฟล์ไม่เจอครับป๋า: {file_name}")

total_sales = calc_total(f'{folder_name}/sales.txt')
print('total sales:', total_sales)

'''ข้อที่ 3: เติมเลขบรรทัด (Read & Write)

โจทย์: จงเขียนฟังก์ชัน add_line_numbers(src_file, dest_file) อ่านไฟล์ต้นฉบับ (src_file) แล้วเขียนลงไฟล์ใหม่ (dest_file) โดยเติมเลขบรรทัดไว้ข้างหน้า

ตัวอย่าง: 1. INFO: System started'''

def add_line_numbers(src_file, dest_file):
    try:
        fn = open(src_file)
        f = open(dest_file, 'w')
        for i, line in enumerate(fn, 1):
            f.write(f'{i}. {line}')        
        f.close()
        fn.close()
    except FileNotFoundError:
        print(f"❌ โอ๊ะ! หาไฟล์ไม่เจอครับป๋า: {src_file}")

add_line_numbers(f'{folder_name}/scores.txt',f'{folder_name}/now_scores.txt')


'''ข้อที่ 4: หาคนเก่งสุด (Find Max)

โจทย์: จงเขียนฟังก์ชัน find_top_student(filename) อ่านไฟล์คะแนน (ชื่อ คะแนน) แล้วคืนชื่อของคนที่ได้คะแนนเยอะที่สุด

Hint: ใช้เทคนิค "King of the hill" (จำค่ามากสุดไว้เทียบ)'''

def find_top_student(file_name):
    try:
        fn = open(file_name)
        count_max = 0
        name_max = ''
        for line in fn:
            student, scores = line.strip('\n').split()
            score = int(scores)
            if count_max < score:
                count_max = score
                name_max = student
        fn.close()
        return name_max
    except FileNotFoundError:
        print(f"❌ โอ๊ะ! หาไฟล์ไม่เจอครับป๋า: {file_name}")

top_score = find_top_student(f'{folder_name}/scores.txt')
print(top_score)
        

'''ข้อที่ 5: ระบบ Login (Search & Validate)

โจทย์: จงเขียนฟังก์ชัน check_login(filename, user, password) รับชื่อและรหัสผ่าน ไปเช็คในไฟล์ว่ามีคู่ user:pass นี้อยู่จริงไหม? (คืนค่า True/False)'''

def check_login(file_name:str, user:str):
    try:
        with open(file_name) as fn:
            for line in fn:
                if user == line.strip('\n'):
                    return True
        return False

    except FileNotFoundError:
        print(f"❌ โอ๊ะ! หาไฟล์ไม่เจอครับป๋า: {file_name}")

print(check_login(f'{folder_name}/users.db', 'paa:password'))
print(check_login(f'{folder_name}/users.db', 'gemini:^&*KGH_'))
