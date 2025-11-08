import random 


def delivery(total_purchase: int, location: str) -> str:
    
    if total_purchase > 2000:
        return f'ยอดสั่งซื้อ {total_purchase} ส่งที่ {location} ส่งฟรี '
    
    elif total_purchase <= 2000:
        if location == 'bkk':
            return f'ยอดสั่งซื้อ {total_purchase} ส่งที่ {location} ค่าส่ง 50 บาท '
            
        else:
            return f'ยอดสั่งซื้อ {total_purchase} ส่งที่ {location} ค่าส่ง 80 บาท '

def call_delivery():

    for item in range(11):
        total_purchase = random.randint(1500,2500)
        location = random.choice(['bkk','upcountry'])
        print(delivery(total_purchase=total_purchase, location=location))
call_delivery()