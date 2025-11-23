import time

# --- 1. เตรียมชุดข้อมูลหลายๆ ชุด (คลังกระสุน) ---
all_test_data = {
    "test_set_1": ["3", "10", "20", "30"],        # สำหรับโจทย์ข้อ 1 (3 รอบ)
    "test_set_2": ["2", "99.9", "1.1"],           # สำหรับโจทย์ข้อ 1 (2 รอบ)
    "test_set_3": ["ณัฐพงศ์", "50000", "DevOps"]    # สำหรับโจทย์ข้อ 2 (โปรไฟล์)
}

# ตัวแปรที่จะถูกดึงไปใช้จริง (เริ่มต้นให้ว่างไว้ก่อน)
mock_inputs = [] 

# --- 2. ฟังก์ชันตัวหลอก (เหมือนเดิมเป๊ะ) ---
def fake_input(prompt_text):
    print(prompt_text, end="")
    time.sleep(0.2) # ปิดไว้จะได้รันไวๆ
    if mock_inputs:
        val = mock_inputs.pop(0)
        print(val)
        return val
    return ""

# สลับร่าง input
input = fake_input

# --- 3. โจทย์ต่างๆ ของป๋า ---

def question_1_loop():
    print("\n--- เริ่มโจทย์ 1: วนลูปรับค่า ---")
    x = []
    n = int(input('round: ')) # จะดึงตัวแรกของ list
    for i in range(1, n+1):
        e = float(input(f'{i} = ')) # ดึงตัวถัดๆ ไป
        x.append(e)
    print("ผลลัพธ์:", x)

def question_2_profile():
    print("\n--- เริ่มโจทย์ 2: รับประวัติ ---")
    name = input("ชื่อ: ")
    salary = input("เงินเดือน: ")
    pos = input("ตำแหน่ง: ")
    print(f"User: {name}, Salary: {salary}, Job: {pos}")

# ==========================================
# 4. วิธีเรียกใช้ (โหลดกระสุน แล้วยิง!)
# ==========================================

# --- การทดสอบรอบที่ 1 ---
# โหลดข้อมูลชุดที่ 1 ใส่เข้าไปใน mock_inputs
mock_inputs = list(all_test_data["test_set_1"]) 
question_1_loop()

# --- การทดสอบรอบที่ 2 (เปลี่ยนข้อมูล แต่ใช้โจทย์เดิม) ---
# โหลดข้อมูลชุดที่ 2
mock_inputs = list(all_test_data["test_set_2"]) 
question_1_loop()

# --- การทดสอบรอบที่ 3 (เปลี่ยนโจทย์ไปเลย) ---
# โหลดข้อมูลชุดที่ 3
mock_inputs = list(all_test_data["test_set_3"]) 
question_2_profile()