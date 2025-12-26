'''แบบฝึกหัด 8-3 ข้อที่ 1
จงเขียนฟังก์ชัน get_countries(capital_city, s) 
รับ capital_city เป็นดิกเก็บข้อมูลในรูปแบบ {ชื่อประเทศ: ชื่อเมืองหลวง} 
และ s เป็นสตริง ฟังก์ชันนี้คืนลิสต์ของชื่อประเทศที่ขึ้นต้นด้วยค่าที่เก็บใน 
s โดยลิสต์ที่คืนเรียงชื่อประเทศจากน้อยไปมากตามพจนานุกรม'''

def get_countries(capital_city, s):
    result = []

    for city in capital_city:
        if city.startswith(s):
            result.append(city)
    result.sort()
    return result

# --- ส่วนทดสอบ (Test Case) ---
# ลองสร้าง Dict ข้อมูลจำลอง
countries = {
    "Thailand": "Bangkok",
    "Turkey": "Ankara",
    "Japan": "Tokyo",
    "Taiwan": "Taipei",
    "China": "Beijing"
}

# ลองเรียกใช้ฟังก์ชัน หาประเทศที่ขึ้นต้นด้วย "T"
print(get_countries(countries, "T"))
# ผลลัพธ์ควรได้: ['Taiwan', 'Thailand', 'Turkey']
'''จุดสังเกต:
การวนลูป for x in dict: จะได้ Key เสมอ ซึ่งตรงกับโจทย์ที่ต้องการเช็ค "ชื่อประเทศ" พอดีครับ
คำสั่ง startswith() จะเช็คตัวพิมพ์เล็ก-ใหญ่ด้วยนะครับ (Case sensitive) เช่น 't' จะไม่เท่ากับ 'T' แต่ปกติโจทย์เกรดเดอร์มักจะให้ใส่ตรงๆ ตามนั้นครับ'''


'''แบบฝึกหัด 8-3 ข้อที่ 2
จงเขียนฟังก์ชัน get_courseIDs(number_of_students, k) 
รับดิก number_of_students ที่เก็บข้อมูลในรูปแบบ 
{รหัสวิชา: จำนวนนิสิตที่ลงทะเบียน} กับ k ที่เป็นจำนวนเต็ม 
ฟังก์ชันนี้คืนลิสต์ของรหัสวิชาต่าง ๆ ที่มีจำนวนผู้ลงทะเบียนเรียนตั้งแต่ k คนขึ้นไป 
โดยให้เรียงรหัสวิชาในลิสต์ที่คืนจากน้อยไปมาก'''

def get_courseIDs(number_of_students, k):
    result = []

    for sid, n in number_of_students.items():
        if n >= k:
            result.append(sid)
    result.sort()
    return result


# Case 1: กรณีปกติ (มีทั้งผ่านและไม่ผ่านเกณฑ์)
# วิชาที่มีคนเรียน >= 30 คน คือ 2110101 (100 คน) และ 2110555 (30 คน)
courses_1 = {'2110101': 100, '2301107': 10, '2110555': 30, '5500111': 29}
print("Test Case 1:", get_courseIDs(courses_1, 30)) 
# ผลที่ควรได้: ['2110101', '2110555'] (เรียงเลขน้อยไปมาก)

# Case 2: กรณีไม่มีวิชาไหนผ่านเกณฑ์เลย (k สูงปรี๊ด)
courses_2 = {'A': 5, 'B': 10, 'C': 2}
print("Test Case 2:", get_courseIDs(courses_2, 100))
# ผลที่ควรได้: []

# Case 3: กรณีผ่านเกณฑ์ทุกวิชา (k ต่ำมาก)
courses_3 = {'SubjectA': 50, 'SubjectB': 60}
print("Test Case 3:", get_courseIDs(courses_3, 1))
# ผลที่ควรได้: ['SubjectA', 'SubjectB']

# Case 4: กรณี Dictionary ว่างเปล่า (ไม่มีข้อมูลเลย)
courses_4 = {}
print("Test Case 4:", get_courseIDs(courses_4, 10))
# ผลที่ควรได้: []

# Case 5: ทดสอบการเรียงลำดับ (Input ไม่เรียง แต่ Output ต้องเรียง)
courses_5 = {'Z999': 50, 'A001': 50, 'M500': 50}
print("Test Case 5:", get_courseIDs(courses_5, 10))
# ผลที่ควรได้: ['A001', 'M500', 'Z999']


'''แบบฝึกหัด 8-3 ข้อที่ 3
จงเขียนฟังก์ชัน add_all(points, blacklist, extra) รับดิก points ที่เก็บข้อมูลในรูปแบบ {รหัสสมาชิก: จำนวนแต้มสะสม}, blacklist เป็นลิสต์เก็บรหัสสมาชิก กับ extra เป็นจำนวนแต้ม ฟังก์ชันนี้จะเพิ่มแต้มเป็นจำนวน extra ในดิก points ให้กับสมาชิกทุกรายที่มีรหัสไม่ปรากฏใน blacklist ฟังก์ชันนี้ไม่คืนอะไรเลย เพราะจะปรับข้อมูลใน points'''

def add_all(points, blacklist, extra):

    for sid, score in points.items():
        if sid not in blacklist:
            points[sid] += extra


# --- พื้นที่ทดสอบ (Test Cases) ---

# Case 1: กรณีปกติ (มีคนโดน Blacklist และคนรอด)
points_1 = {'A': 100, 'B': 200, 'C': 300}
blacklist_1 = ['A', 'C']
add_all(points_1, blacklist_1, 50)
print("Test Case 1:", points_1)
# ผลที่ควรได้: {'A': 100, 'B': 250, 'C': 300} 
# (B ได้เพิ่ม 50, ส่วน A กับ C อดเพราะติด Blacklist)

# Case 2: กรณีไม่มีใครติด Blacklist เลย
points_2 = {'X': 10, 'Y': 20}
blacklist_2 = []
add_all(points_2, blacklist_2, 100)
print("Test Case 2:", points_2)
# ผลที่ควรได้: {'X': 110, 'Y': 120} (ทุกคนได้หมด)

# Case 3: กรณีโดน Blacklist กันหมด
points_3 = {'M1': 5, 'M2': 5}
blacklist_3 = ['M1', 'M2', 'M3']
add_all(points_3, blacklist_3, 10)
print("Test Case 3:", points_3)
# ผลที่ควรได้: {'M1': 5, 'M2': 5} (คะแนนเท่าเดิมทุกคน)

# Case 4: กรณีแต้มติดลบ (โดนหักคะแนน)
points_4 = {'Hero': 100, 'Villain': 100}
blacklist_4 = ['Villain']
add_all(points_4, blacklist_4, -50) # extra เป็น -50
print("Test Case 4:", points_4)
# ผลที่ควรได้: {'Hero': 50, 'Villain': 100} (Hero โดนลด, Villain รอดเพราะติด Blacklist)

# Case 5: Dictionary ว่างเปล่า
points_5 = {}
add_all(points_5, ['A'], 100)
print("Test Case 5:", points_5)
# ผลที่ควรได้: {}