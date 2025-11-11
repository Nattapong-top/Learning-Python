import random


'''
🚦 โจทย์ if / elif / else 10 ข้อ (ตรรกะ IT Support)
📝 โจทย์ที่ 1: การตรวจสอบสถานะการเชื่อมต่อ
สถานการณ์: ป๋าเขียนสคริปต์เพื่อตรวจสอบสถานะของเซิร์ฟเวอร์ ถ้า ping_status เป็น 0 หมายถึง Success, ถ้าเป็น 1 หมายถึง Timeout, ถ้าเป็น 2 หมายถึง Host Unreachable
'''
def check_ping(status:int) -> str:
    if status == 0:
        return f'Status: {status} = Success'
    elif status == 1:
        return f'Status: {status} = Timeout'
    elif status == 2:
        return f'Status: {status} = Host Unreachable'
    else:
        return f'Status: {status} = Error'

def call_check_ping():
    status = random.randint(0,3)
    print(check_ping(status=status))
call_check_ping()


'''
📝 โจทย์ที่ 2: การจัดการ Disk Space Alert
สถานการณ์: ป๋าต้องตั้งค่าการแจ้งเตือน Disk Space
เกิน 90% และ น้อยกว่าหรือเท่ากับ 100% -> CRITICAL
เกิน 70% และ น้อยกว่าหรือเท่ากับ 90% -> WARNING
น้อยกว่าหรือเท่ากับ 70% -> NORMAL
'''
def check_disk(using:int) -> str:
    if using > 90 :
        return f'Disk {using}% = CRITICAL'
    elif using > 70:
        return f'Disk {using}% = WARNING'
    elif using <= 70:
        return f'Disk {using}% = NORMAL'

def call_check_disk():
    using = random.randint(60,100)
    print(check_disk(using=using))
call_check_disk()

'''
📝 โจทย์ที่ 3: การตรวจสอบ Log Level แบบ Case-Insensitive
สถานการณ์: ป๋าต้องตรวจสอบ log_entry ที่มาจากหลายแหล่ง ถ้ามีคำว่า "error" หรือ "failure" ปรากฏอยู่ (ไม่ว่าจะเป็นตัวพิมพ์เล็ก/ใหญ่) ให้แสดง "Action Needed"
'''
def check_log(log:str) -> str:
    
    if 'error' in log.lower() or 'failure' in log.lower():
        return f'Log: {log} = Action Needed'
    else:
        return f'Log: {log} = Not Found'

def call_check_log():
    log_entry =  ['ERROR','FAILURE','หกดเหกดเหดกดเกดเ', 'sdfgsdfgsdfg']

    log = random.choice(log_entry)

    print(check_log(log=log))
call_check_log()

'''
📝 โจทย์ที่ 4: การกำหนดสิทธิ์เข้าถึง (Nested If)
สถานการณ์: การเข้าถึงไฟล์ Configuration ต้องผ่าน 2 เงื่อนไข: 1. ต้องเป็น is_staff เป็น True 2. ต้องมาจาก source_ip ที่เป็น "192.168.1.5" เท่านั้น
'''
def check_ip(is_staff:str, ip:str) -> str:
    if is_staff and ip == '192.168.1.5':
        return f'IP: {ip} Saff: {is_staff} = Access Granted'
    else:
        return f'IP: {ip} Saff: {is_staff} = Not Access'

def call_check_ip():
    ip = random.choice(['192.168.1.5', '192.168.1.6'])
    is_saff = random.choice([True, False])

    access = check_ip(is_staff=is_saff, ip=ip)

    print(access)
call_check_ip()

'''
📝 โจทย์ที่ 5: การตรวจสอบช่วงเวลาทำงาน (Working Hours)
สถานการณ์: ป๋าต้องอนุญาตให้สคริปต์ Backup ทำงานได้ระหว่าง 22:00 น. ถึง 06:00 น. (ตัวแปร current_hour คือชั่วโมง 0-23)

โจทย์: จงเลือกโค้ดที่ถูกต้องที่สุดเมื่อ current_hour = 4 (ตี 4)
'''

def work_hours(current_hours:int) -> str:
    if current_hours >= 22 or current_hours <= 6:
        return f'Current Hours: {current_hours} = Backup'
    else:
        return f'Current Hours: {current_hours} = Not Backup'

def call_work_hours():
    current_hours = random.randint(0,24)

    print(work_hours(current_hours=current_hours))

call_work_hours()
