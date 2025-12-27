# แบบฝึกหัด 8-3 : for k in a_dict (พื้นฐาน)
# สไตล์สอบ Grader จุฬาฯ
# เขียนเฉพาะฟังก์ชัน ห้าม print ห้าม input


def get_keys_startwith(d, s):
    """
    d เป็น dict {key: value}
    s เป็น string

    คืน list ของ key ทั้งหมดใน d ที่ขึ้นต้นด้วย s
    โดยเรียงลำดับ key จากน้อยไปมาก
    """
    result = []
    for k in d:
        if k.startswith(s):
            result.append(k)
    result.sort()
    return result

countries = {
    "Thailand": "Bangkok",
    "Turkey": "Ankara",
    "Japan": "Tokyo",
    "Taiwan": "Taipei",
    "China": "Beijing"
}
print(get_keys_startwith(countries, 'T'))

def count_keys_longer_than(d, n):
    """
    d เป็น dict ที่ key เป็น string
    n เป็นจำนวนเต็ม

    คืนจำนวน (int) ของ key ที่มีความยาวมากกว่า n
    """
    total = 0
    for k in d.keys():
        if len(k) > n:
            total += 1
    return total

print(count_keys_longer_than(countries, 5))

def get_keys_by_value(d:dict, v):
    """
    d เป็น dict
    v เป็นค่าที่ต้องการตรวจสอบ

    คืน list ของ key ที่มี value เท่ากับ v
    โดยเรียง key จากน้อยไปมาก
    """
    result = []
    for k, c in d.items():
        if c == v:
            result.append(k)
    result.sort()
    return result

print(get_keys_by_value(countries, 'Bangkok'))


def remove_keys(d:dict, blacklist:list):
    """
    d เป็น dict
    blacklist เป็น list ของ key

    ให้ลบ key ใน blacklist ออกจาก d
    ฟังก์ชันไม่ต้องคืนค่า (แก้ d โดยตรง)
    """
    # pass
    del_d = []
    for k in d:
        if k in blacklist:
            del_d.append(k)
    
    for i in del_d:
        del d[i]
    
    # return d

del_county = ['Taiwan', 'China']
# print(remove_keys(countries, del_county))
remove_keys(countries, del_county)


def sum_values_of_selected_keys(d:dict, keys:list):
    """
    d เป็น dict {key: number}
    keys เป็น list ของ key

    คืนผลรวมของ value เฉพาะ key ที่อยู่ใน keys
    (ถ้า key ใดไม่มีใน d ให้ข้าม)
    """
    # pass
    total = 0
    for k, val in d.items():
        if k in keys:
            total += val
    return total

total_d = {'a':10, 'b':20, 'c':30, 'j':50}
keys_of_sum = ['a','b','c']
print(sum_values_of_selected_keys(total_d, keys_of_sum))