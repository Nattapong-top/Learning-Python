'''แบบฝึกหัด 8-2 ข้อที่ 1
จงสร้างตัวแปรชื่อ count_alpha เป็นดิกที่มี key เป็นตัวอักษรอังกฤษทั้งใหญ่และเล็กทุกตัวอักษร ส่วน value ให้เป็น 0 หมด'''

count_alpha = {}
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha += alpha.lower()
for c in alpha:
    count_alpha[c] = 0
print(count_alpha)


'''แบบฝึกหัด 8-2 ข้อที่ 2
มีดิกชื่อ number_of_students อยู่แล้วตัวหนึ่ง จัดเก็บข้อมูลในรูปแบบ {รหัสวิชา: จำนวนนิสิตที่ลงทะเบียน} 
โดยรหัสวิชาเป็นสตริง จงเขียนคำสั่งเพิ่มจำนวนนิสิตที่ลงทะเบียนให้กับวิชา 2110101 อีก 28 คน และตั้งให้วิชา 
2301107 มีนิสิตลงทะเบียน 824 คน'''

number_of_students = {'2110101': 440, '2110211': 120, '2110183': 7}
print(number_of_students)

number_of_students['2110101'] += 28
number_of_students['2301107'] = 824

print(number_of_students)

'''แบบฝึกหัด 8-2 ข้อที่ 3
โปรแกรมนี้มีตัวแปร student1 เป็นดิกเก็บรายละเอียดของนักเรียนคนหนึ่ง จงเขียนฟังก์ชัน read_data() 
มีหน้าที่อ่านข้อมูลจากอินพุตประกอบด้วย เลขประจำตัว, ชื่อ-สกุล, วัน, เดือน, ปีเกิด (คั่นด้วย comma 
และช่องว่าง) มาเก็บในดิกที่มีรูปแบบเดียวกับ student1 แล้วคืนเป็นผลของฟังก์ชัน 
เช่น อินพุตเป็น 4230000021, Natalie P., 9, 6, 1981 จะได้ผลจาก read_data 
เป็น {"ID": "4230000021", "Name": "Natalie P.", "Birthdate": [9, 6, 1981]}'''

# สูตรอาจารย์

def read_data():
    x = '4230000021, Natalie P., 9, 6, 1981'.split(", ")
    r = {}
    r["ID"] = x[0]
    r["Name"] = x[1]
    r["Birthdate"] = [int(x[2]), int(x[3]), int(x[4])]
    return r
print(read_data())

# สูตรป๋าเขียนเอง
def read_data():
    x = '4230000021, Natalie P., 9, 6, 1981'.split(", ")
    bdt = [int(x[2]),int(x[3]),int(x[4])]
    student2 = {'ID': x[0], 
                'Name': x[1], 
                'Birthdate': bdt }
    return student2
print(read_data())