# ============================================
# แบบฝึกหัด 8-3 : for k in a_dict (เพิ่มระดับ)
# สไตล์สอบ Grader จุฬาฯ
# --------------------------------------------
# ส่วนบน: ฟังก์ชัน (ห้าม print / input)
# ส่วนล่าง: Test Case (ใช้ run ดูผลได้)
# ============================================


def invert_unique(d:dict):
    """
    d เป็น dict {key: value}

    คืน dict ใหม่ที่สลับ key กับ value
    เฉพาะคู่ที่ value ไม่ซ้ำกันเท่านั้น
    """
    # นับก่อน เพื่อรู้ว่าใครซ้ำ → แล้วค่อยวนอีกรอบเพื่อ “เลือกเฉพาะที่ไม่ซ้ำ”
    count = {}
    for v in d.values():
        count[v] = count.get(v, 0) + 1
    
    new_d = {}
    for key, val in d.items():
        if count[val] == 1:
            new_d[val] = key
    return new_d

def update_scores(scores, passed_ids, bonus):
    """
    scores เป็น dict {id: score}
    passed_ids เป็น list ของ id
    bonus เป็นจำนวนคะแนน

    เพิ่ม bonus ให้เฉพาะ id ที่อยู่ใน passed_ids
    ฟังก์ชันไม่ต้องคืนค่า (แก้ scores โดยตรง)
    """
    for k in scores:
        if k in passed_ids:
            scores[k] += bonus

def get_max_keys(d:dict):
    """
    d เป็น dict {key: number}

    คืน list ของ key ที่มี value มากที่สุด
    โดยเรียง key จากน้อยไปมาก
    """
    # ถ้าเจอค่ามากกว่าเดิม → ล้าง list
    # ถ้าเจอค่าเท่ากัน → append
    key_max = 0
    key_name = []
    for k, val in d.items():
        if val > key_max:
            key_max = val
            key_name = [k]
        elif val == key_max:
            key_name.append(k)
    key_name.sort()
    return key_name

# เขียนแบบ pythonic
def get_max_keys_pythonic(d:dict):
    best = None     # เอาไว้เปรียบเที่ยบคะแนนสูงสุด ตอนนี้ยังไม่มี
    keys = []       # เก็บชื่อแชมป์ + ผู้ท้าชิงที่เสมอ

    for k, v in d.items():
        if best is None or v > best:
            best = v
            keys = [k]
        elif v == best:
            keys.append(k)
    
    keys.sort()
    return keys



def remove_by_value(d:dict, v):
    """
    d เป็น dict
    v เป็นค่าที่ต้องการลบ

    ให้ลบทุก key ที่มี value เท่ากับ v ออกจาก d
    ฟังก์ชันไม่ต้องคืนค่า
    """
    del_v = []
    for key, val in d.items():
        if val == v:
            del_v.append(key)

    for k in del_v:
        del d[k]


def count_value_groups(d):
    """
    d เป็น dict {key: value}

    คืน dict ใหม่ในรูปแบบ
    {value: จำนวน key ที่มี value นั้น}
    """
    new_d = {}
    for k, v in d.items():
        new_d[v] = new_d.get(v, 0) + 1
    
    return new_d


# ============================================
# Test Area (โหมดฝึก / Debug / GitHub)
# ============================================
if __name__ == "__main__":

    print("=== Test invert_unique ===")
    d1 = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
    print(invert_unique(d1))
    # ควรได้: {2: 'b', 3: 'd'}

    print("\n=== Test update_scores ===")
    scores = {'A': 50, 'B': 60, 'C': 70}
    update_scores(scores, ['A', 'C'], 10)
    print(scores)
    # ควรได้: {'A': 60, 'B': 60, 'C': 80}

    print("\n=== Test get_max_keys ===")
    d2 = {'x': 10, 'y': 20, 'z': 20, 'a': 5}
    print(get_max_keys(d2))
    # ควรได้: ['y', 'z']
    print(get_max_keys_pythonic(d2))

    print("\n=== Test remove_by_value ===")
    d3 = {'p': 1, 'q': 2, 'r': 1, 's': 3}
    remove_by_value(d3, 1)
    print(d3)
    # ควรได้: {'q': 2, 's': 3}

    print("\n=== Test count_value_groups ===")
    d4 = {'a': 1, 'b': 1, 'c': 2, 'd': 2, 'e': 2}
    print(count_value_groups(d4))
    # ควรได้: {1: 2, 2: 3}
