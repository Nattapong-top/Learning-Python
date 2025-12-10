'''ข้อที่ 1: คำนวณยอดจ่ายเงินเดือน (Aggregation)
โจทย์: เขียนฟังก์ชัน calculate_payroll(salaries)
- รับ List ของเงินเดือนพนักงานเข้ามา
- คืนค่า (Return) ผลรวมเงินเดือนทั้งหมดที่ต้องจ่าย
(ถ้าป๋าอยากลองวิชา: ลองเขียนแบบใช้ sum() บรรทัดเดียวดูครับ)'''

def calculate_payroll(salaries):
    # เขียนโค้ดตรงนี้
    total = 0
    for n in salaries:
        total += n
    return total #sum(salaries)

# ทดสอบ
staff_salaries = [15000, 23000, 18000, 50000]
print(staff_salaries)
print(f"ยอดจ่ายรวม: {calculate_payroll(staff_salaries)}")


'''ข้อที่ 2: คัดกรองสินค้าราคาแพง (Filtering)
โจทย์: เขียนฟังก์ชัน get_expensive_items(prices, limit)
- รับ List ราคาสินค้า (prices) และ เพดานราคา (limit)
- คืนค่า List ใหม่ ที่มีเฉพาะราคาที่ "แพงกว่า" limit เท่านั้น'''

def get_expensive_items(prices, limit):
    prices_over_limit = []

    for p in prices:
        if p > limit:
            prices_over_limit.append(p)
    
    return prices_over_limit #[p for p in prices if p > limit] 

# ทดสอบ
all_prices = [100, 50, 300, 20, 500, 1000]
print(f"สินค้าราคาเกิน 400: {get_expensive_items(all_prices, 400)}")


'''ข้อที่ 3: ปรับเงินเดือนพนักงาน (Mapping)
โจทย์: เขียนฟังก์ชัน increase_salary(salaries)
- รับ List เงินเดือนเดิมเข้ามา
- คืนค่า List ใหม่ ที่เงินเดือนทุกก้อนถูก "เพิ่มขึ้น 10%" (คูณ 1.1)
- (เอาทศนิยมออกด้วยการแปลงเป็น int ก็ดีครับ)'''

def increase_salary(salaries):
    # Hint: ใช้ List Comprehension คำนวณค่าใหม่
    return [int(e*1.1) for e in salaries]

# ทดสอบ (ใช้ข้อมูลจากข้อ 1)
print(f"ฐานเงินเดือนใหม่ (+10%): {increase_salary(staff_salaries)}")


'''ข้อที่ 4: ตรวจสินค้าหมดอายุ (Boolean Logic on List)
โจทย์: เขียนฟังก์ชัน has_expired(dates, current_year)
- รับ List ปีที่หมดอายุ (dates) และ ปีปัจจุบัน (current_year)
- ถ้าเจอสินค้าตัวไหนที่ปี "น้อยกว่า" ปีปัจจุบัน (คือหมดอายุแล้ว) ให้ Return True ทันที
- ถ้าเช็คจนครบแล้วไม่เจอเลย ให้ Return False'''

def has_expired(dates, current_year):
    # Hint: วนลูปเช็ค ถ้าเจอ dates[i] < current_year ให้ return True
    # หรือจะใช้ any() ก็เท่ครับ
    for i in dates:
        if i < current_year: 
            return True
    
    return False
            #any(i < current_year for i in dates)

# ทดสอบ
stock_years = [2026, 2027, 2024, 2028]
print(f"มีของหมดอายุ (เทียบปี 2025) ไหม?: {has_expired(stock_years, 2025)}")


'''ข้อที่ 5: ตัดเกรดทั้งห้อง (Complex Logic)
โจทย์: เขียนฟังก์ชัน grade_class(scores)
- รับ List คะแนนสอบ (0-100)
- คืนค่า List ของเกรด ['A', 'F', 'P', ...] โดยมีเกณฑ์:
  >= 80 ได้ 'A'
  >= 50 ได้ 'P'
  < 50 ได้ 'F'
(ข้อนี้ป๋าอาจต้องเขียนฟังก์ชันย่อยช่วย หรือเขียน Logic ใน Loop ก็ได้ครับ)'''

def grade_class(scores):
    # สร้าง list ว่าง
    # วนลูปคะแนน
    #   เช็คเกรด -> append ใส่ list
    # return list
    # grades = []
    # for g in scores:
    #     if g >= 80:
    #         grades.append('A')
    #     elif g >= 50:
    #         grades.append('P')
    #     else:
    #         grades.append('F')
    # return grades

    return [check_scores(g) for g in scores]

def check_scores(score):
    if score >= 80:
        return 'A'
    elif score >= 50:
        return 'P'
    else:
        return 'F'

# ทดสอบ
student_scores = [45, 90, 60, 80, 30]
print(f"เกรดทั้งห้อง: {grade_class(student_scores)}")