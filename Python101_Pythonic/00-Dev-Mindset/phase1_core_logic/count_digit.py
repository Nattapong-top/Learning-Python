

def count_digit(raw_list:list, d:int):
    count = 0
    for n in raw_list:
        if isinstance(n, int):
            num = abs(n)
            while num > 0:
                digit = num % 10
                if digit == d:
                    count += 1
                num //= 10
    return count
raw_list = raw_list = [2456, 34, 5, 6, 5, 53356645, 444, 0, 000]
print(count_digit(raw_list, 0))

# -------------------------------------------------

'''โค้ดระดับโปรดักชัน'''

def count_digit_production(raw_list:list, d:int):
    if not isinstance(d, int) or not (0 <= d <=9):
        raise ValueError('d ไม่ใช่ตัวเลขจำนวนเต็มหรือไม่ได้อยู่ระหว่าง 0 - 9')
    
    count = 0

    for n in raw_list:
        if not isinstance(n, int):
            continue

        num = abs(n)

        # วิธีรับมือกับ d = 0 เนื่องจาก while จะไม่ทำงาน
        # จึงต้องแยก 0 มานับนอก while
        if num == 0:
            if d == 0:
                count += 1
        
        while num > 0:
            digit = num % 10
            if digit == d:
                count += 1
            num //= 10
    return count
print(count_digit_production(raw_list, 0))
