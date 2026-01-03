'''โจทย์ (TH):
รับข้อมูลจากผู้ใช้ทีละบรรทัด
แต่ละบรรทัดอาจมีหลายค่า (คั่นด้วยช่องว่าง)
จบเมื่อผู้ใช้พิมพ์ END
ให้นับว่า “มีตัวเลขจำนวนเต็มกี่ตัวทั้งหมด”'''

def count_valid_numbers():
    counter = 0
    while True:
        raw_line = input('input: ')
        if not raw_line:
            continue
        elif raw_line.upper() == 'END':
            break
        else:
            parts = raw_line.split()        
            for num in parts:
                if num.lstrip('-').isdigit():
                    counter += 1
    return counter
print(count_valid_numbers())