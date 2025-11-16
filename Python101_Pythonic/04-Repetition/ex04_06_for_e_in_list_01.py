'''📝 โจทย์ฝึก 4.6 (5 ข้อ)
เพื่อให้ป๋าได้ฝึกประยุกต์ใช้กับ List โดยตรง ผมขอให้ป๋าลองทำ 5 
โจทย์นี้ครับ โดยใช้โครงสร้าง for item in list_name::
นับเลขติดลบ:
ข้อมูล: numbers = [10, -5, 2, -10, 0, 7]
เป้าหมาย: นับว่ามี จำนวนเต็มลบ อยู่ใน List กี่ตัว'''
def count_negative():
    numbers = [10, -5, 2, -10, 0, 7]
    count = 0
    for e in numbers:
        if e < 0:
            count += 1

    print('negarive =',count)
count_negative()
print('============ End Function ============\n')

'''2. หาผลรวม:
ข้อมูล: prices = [100.5, 250, 499.99, 1000]
เป้าหมาย: หา ผลรวม ของราคาทั้งหมดใน List (Accumulator Pattern)'''
def total_sum():
    prices = [100.5, 250, 499.99, 1000]
    result = 0

    for num in prices:
        result += num

    result_sum = sum(prices)

    print('result =', result)
    print('result sum =', result_sum)

total_sum()
print('============ End Function ============\n')

'''กรองเฉพาะชื่อ:
ข้อมูล: mixed_data = ["file.txt", "admin", 101, "guest", 99]
เป้าหมาย: สร้าง List ใหม่ ที่มีเฉพาะข้อมูลประเภท String เท่านั้น'''
def filter_str():
    mixed_data = ["file.txt", "admin", 101, "guest", 99]

    str_data = []

    for ch in mixed_data:

        
        # if type(ch) == str:
        if isinstance(ch, str):
            str_data.append(ch)
        

    print('string data =', str_data)
    print('string data =', '|',' | '.join(str_data), '|')
filter_str()
print('============ End Function ============\n')


'''4. หาความเสี่ยง:
ข้อมูล: risk_scores = [5, 12, 1, 8, 15, 3]
เป้าหมาย: ตรวจสอบว่าใน List มี Score ที่ "สูงเกินเกณฑ์" (เกิน 10) หรือไม่ (ใช้ Boolean Flag และ break เหมือนข้อ 5)'''
def check_risk_scores():
    risk_scores = [5, 12, 1, 8, 15, 3]
    is_risk = False

    for risk in risk_scores:
        if risk > 10:
            is_risk = True
            print('Risk score =', risk)
            break
    
    print('Risk =', is_risk)
check_risk_scores()
print('============ End Function ============\n')


'''การปรับปรุงข้อมูล:
ข้อมูล: users = ["Tom", "jerry", "spike"]
เป้าหมาย: สร้าง List ใหม่ ที่มีชื่อผู้ใช้โดย เปลี่ยนอักษรตัวแรกเป็นพิมพ์ใหญ่ ทั้งหมด
คำใบ้: ป๋าจะต้องใช้ item[0].upper() + item[1:]'''
def username_upper():
    users = ["Tom", "jerry", "spike"]
    new_user = []

    for name in users:
        new_user.append(name[0].upper() + name[1:])
    
    print('New User = ', new_user)
    print('New User = ', ' '.join(new_user))
username_upper()
print('============ End Function ============\n')



