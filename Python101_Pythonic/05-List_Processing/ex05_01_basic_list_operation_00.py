'''แบบฝึกหัด 5-1 ข้อที่ 1
มีข้อมูลทาง input สามบรรทัด บรรทัดแรกเป็นรายการของรหัสสินค้า 
บรรทัดที่สองเป็นรายการของราคา (มีจำนวนข้อมูลเท่ากับของบรรทัดแรก 
โดยสินค้าชิ้นที่ตำแหน่ง i ก็มีราคาที่ตำแหน่ง i) 
บรรทัดสุดท้ายเป็นรหัสสินค้าที่อยากรู้ว่าราคาเท่าไร ถ้าเป็นรหัสที่ไม่มีอยู่ 
ให้แสดง Not found
A100 A200 A300 A400
20.5 50.0 35.0 65.0
'''
def found_product():
    prod_id = input('product = ').split()
    prices = input('ราคา = ').split()
    qid = input('Found product = ').upper()
    found = False

    for i in range(len(prod_id)):
        if qid == prod_id[i]:
            found = True
            break
    
    if found:
        print('product = ',prod_id[i], prices[i])
    else:
        print('Not Found')

# found_product()


''''
แบบฝึกหัด 5-1 ข้อที่ 2
ลักษณะข้อมูลเหมือนข้อที่แล้ว แต่บรรทัดที่สามจะเป็นราคา 
แล้วอยากให้หาว่ามีรหัสสินค้าอะไรบ้างที่ราคาไม่เกินราคาที่กำหนดในบรรทัดที่สาม 
โดยให้แสดงรหัสสินค้าเรียงตามที่เขียนในบรรทัดแรก แสดงบรรทัดละรหัส 
ถ้าไม่มีรหัสสินค้าใดเลย ให้แสดง Not found (จากตัวอย่างที่แสดง จะแสดงรหัสสินค้า 
A100, A200 และ A300 บรรทัดละรหัส
A100 A200 A300 A400
20.5 50.0 35.0 65.0
'''

def check_price_then_50(prod_id:str, x:str, qprice:str):
    prod_id = prod_id.split()
    x = x.split()
    found = False

    prices = [0.0] * len(x)

    for i in range(len(prices)):
        
        prices[i] = float(x[i])

        if prices[i] <= float(qprice):
            print(prod_id[i])
            found = True

    if not found:
        print('Not found')
    
prod_id = 'A100 A200 A300 A400'
price = '20.5 50.0 35.0 65.0'
qprice  = '55.0'
check_price_then_50(prod_id=prod_id, x=price, qprice=qprice)
