'''
📝 โจทย์ท้าทาย: การประมวลผล Configuration File (User Access)
สมมติว่าป๋ามี Python Dictionary ที่จำลองข้อมูลการตั้งค่าสิทธิ์การเข้าถึงของผู้ใช้ในระบบ (คล้ายกับข้อมูลในไฟล์ /etc/passwd หรือ Active Directory)

🎯 เป้าหมายของสคริปต์ (Output)
จงเขียน for loop เพื่อวนซ้ำผ่าน user_configs และใช้ if/elif/else ในการระบุว่า User แต่ละคนควรถูก "ยกเลิกการเข้าถึง" (Decommission) หรือ "แจ้งเตือน" (Alert) หรือ "คงไว้" (Keep) ตามกฎต่อไปนี้:

กฎ Decommission: User จะต้องถูก ยกเลิกการเข้าถึง ถ้าสถานะเป็น 'inactive' และ last_login (จำนวนวันที่ไม่ได้เข้าใช้งาน) มากกว่า 60 วัน

กฎ Alert: User จะต้องถูก แจ้งเตือน ถ้าสถานะเป็น 'active' แต่ role เป็น 'guest'

กฎ Keep: นอกเหนือจากเงื่อนไขข้างต้น ให้ คงไว้
'''
def user_access():
    user_configs = {
        'tom.cat': {'status': 'active', 'role': 'admin', 'last_login': 5},
        'jerry.mouse': {'status': 'inactive', 'role': 'user', 'last_login': 30},
        'spike.dog': {'status': 'active', 'role': 'admin', 'last_login': 1},
        'tyke.dog': {'status': 'active', 'role': 'guest', 'last_login': 60},
        'butch.cat': {'status': 'inactive', 'role': 'user', 'last_login': 90},
        }
    
    # วนซ้ำผ่าน Key (username) และ Value (config details) พร้อมกัน
    for username, config in user_configs.items():

        # ดึงค่ามาเก็บไว้ในตัวแปรย่อยเพื่อให้อ่านง่ายขึ้น
        status = config['status']
        role = config['role']
        last_login = config['last_login']

        # --- เริ่มต้น If/Elif/Else Logic ตรงนี้ ---

        # 1. กฎ Decommission (inactive AND last_login > 60)
        if status == 'inactive' and last_login > 60:
            print(f'[DECOMMISSION] {username}: Inactive และไม่ได้เข้าสู่ระบบ {last_login} วัน')

        # 2. กฎ Alert (active BUT role is guest)
        # ใช้ elif เพื่อไม่ให้ตรวจสอบเงื่อนไขนี้ ถ้า User ถูก Decommission ไปแล้ว
        elif status =='active' and role == 'guest':
            print(f'[ALERT] {username}: User Active แต่มี Role เป็น Guest ควรตรวจสอบสิทธิ์')

        # 3. กฏ Keep (ที่เหลือ)
        else:
            print(f'[KEEP] {username}: สถานะปกติ')

# user_access()

'''
📝 โจทย์ฝึกฝน 5 ข้อ: การจัดการ Config และ User Data
ข้อมูล Configuration (Input สำหรับทุกข้อ)
'''

network_devices = {
        'RTR-HQ-01': {'status': 'up', 'role': 'router', 'uptime_days': 500},
        'SW-Branch-05': {'status': 'down', 'role': 'switch', 'uptime_days': 5},
        'AP-Cafe': {'status': 'up', 'role': 'ap', 'uptime_days': 120},
        'FW-DMZ-02': {'status': 'up', 'role': 'firewall', 'uptime_days': 30},
        'RTR-Backup': {'status': 'up', 'role': 'router', 'uptime_days': 400},
        }

'''
1. ⚙️ การตรวจสอบ Uptime และ Role
โจทย์: จงเขียนโค้ดที่ตรวจสอบอุปกรณ์แต่ละชิ้นใน network_devices ตามเงื่อนไข:

ถ้าอุปกรณ์เป็น 'router' และ มี uptime_days เกิน 365 วัน ให้แสดง "CRITICAL: Router needs Reboot"

ถ้าเป็น 'switch' และ uptime_days น้อยกว่า 30 วัน ให้แสดง "INFO: New Switch, Monitoring"

นอกเหนือจากนั้น ให้แสดง "OK"
'''

def check_uptime():

    for devices, values in network_devices.items():

        status = values['status']
        role = values['role']
        uptime_days = values['uptime_days']

        print(f'Status: {status:5} Role: {role:9} Uptime days: {uptime_days}')

        if role == 'router' and uptime_days > 365:
            print(f'   CRITICAL: {devices} Router needs Reboot')
        
        elif role == 'switch' and uptime_days < 30:
            print(f'   INFO: {devices} New Switch, Monitoring')

        else:
            print(f"   {devices} Is' OK")
        print()

# check_uptime()

'''
2. 🚨 การแจ้งเตือนสถานะ Down และ Role
โจทย์: จงเขียนโค้ดเพื่อระบุลำดับความสำคัญของ Alert เมื่ออุปกรณ์มีสถานะ 'down':

ถ้า status เป็น 'down' และ role เป็น 'firewall' หรือ 'router' ให้แสดง "PRIORITY 1: Down Core Device"

ถ้า status เป็น 'down' แต่ role เป็น 'switch' หรือ 'ap' ให้แสดง "PRIORITY 2: Down Access Device"

นอกเหนือจากนั้น ให้แสดง "All Up"
'''

def check_status():

    for devivce, values in network_devices.items():

        status = values["status"]
        role = values["role"]

        if status == 'down' and role in ['firewall', 'router']:
            print(f'{devivce} PRIORITY 1: {role} Down Core Device')
        
        elif status == 'down' and role in ['switch', 'ap']:
            print(f'{devivce} PRIORITY 2: {role} Down Access Dvice')
        
# check_status()

'''
3. 📉 การกรองอุปกรณ์ที่ต้องอัพเกรด (Using continue)
โจทย์: จงเขียนโค้ดที่แสดงผลเฉพาะอุปกรณ์ที่มี role เป็น 'router' หรือ 'firewall' เท่านั้น โดยใช้คำสั่ง continue เพื่อข้ามอุปกรณ์อื่น ๆ และเมื่อพบแล้วให้แสดง "CHECK: Potential Upgrade Candidate"
'''
def check_role():

    for _, values in network_devices.items():

        role = values['role']

        if role not in ['router', 'firewall']:
            print(f'{role} ข้าม')
            continue 
        elif role in ['router', 'firewall']:
            print(f"CHECK: {role} Potential Upgrade Candidate")

check_role()

'''
4. 🔀 การสลับค่า Role (Conditional Update)
โจทย์: จงเขียนโค้ดที่วนซ้ำ Dictionary และ อัพเดต ค่า role ของอุปกรณ์ เฉพาะ ที่มี status เป็น 'down' ให้เป็น 'DECOMMISSIONED'

(ข้อนี้ต้องทำสำเนา Dictionary ก่อนการวนซ้ำ เพราะเรากำลังแก้ไข Dictionary ที่กำลังวนซ้ำอยู่)
'''
def check_status_down():
    devices_to_update = network_devices.copy()
    print('\n ---- 4. การ Decommission อุปกรณ์ ----')

    for device, config in devices_to_update.items():
        
        if config['status'] == 'down':

            devices_to_update[device]['role'] = 'DECOMMISSIONED'
            print(f'[{device}] Role ถูกเปลี่ยนเป็น DECOMMISSIONED')
check_status_down()


'''
# ใช้ .copy() เพื่อสร้างสำเนาสำหรับแก้ไขในลูป
devices_to_update = network_devices.copy() 
5. ⚠️ การตรวจสอบ Uptime ครบปี (ใช้ Modulus)
โจทย์: จงเขียนโค้ดที่ตรวจสอบอุปกรณ์แต่ละชิ้น และ:

ถ้า uptime_days หาร 365 ลงตัว (แสดงว่ารันมาครบปีพอดี) ให้แสดง "REBOOT SCHEDULE: Anniversary Uptime"

นอกเหนือจากนั้น ให้แสดง "Uptime: X days"
'''

def check_anniversary_uptime():
    print('\n ---- 5. ตรวจสอบ Uptime ครบรอบปี ----')

    for device, config in network_devices.items():
        days = config['uptime_days']

    if days % 356 == 0 and days > 0:
        print(f'{device}: REBOOT SCHEDULE: Anniversary Uptime ({days} days)')
    else:
        print(f'{device}: Uptime: {days} days')
check_anniversary_uptime()