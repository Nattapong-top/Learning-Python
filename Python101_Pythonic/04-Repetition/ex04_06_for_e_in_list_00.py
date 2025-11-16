'''โจทย์ for e in list จากเว็บ จุฬา'''
'''กำหนดให้มีรายการรหัสสินค้าจาก input (คั่นด้วยช่องว่าง) 
เช่น A1023 P223 A392 จงเขียนโปรแกรมอ่านรหัสสินค้าจาก 
input นำรหัสสินค้าจากซ้ายไปขวามาแสดงบรรทัดละหนึ่งรหัส
E101 E123 E323 E493 E928 E883'''
def check_product(prod_ids:str):

    # แบบธรรมดา เอามา split() ก่อนแล้วค่อยไป for
    #prod_list = prod_ids.split()

    # เราสามารถ split() ที่  for เลยก็ได้
    for e in prod_ids.split():
        print('Product ID:', e)
    
check_product('E101 E123 E323 E493 E928 E883')
print('============ End Function ============\n')


'''กำหนดให้มีรายการรหัสสินค้าจาก 
input (เริ่มด้วยประเภทสินค้าตามด้วย : ตามด้วยรหัสสินค้าคั่นด้วยช่องว่าง) 
เช่น Office Product: A1023 P223 A392 จงเขียนโปรแกรมอ่านรหัสสินค้าจาก 
input นำเฉพาะรหัสสินค้าจากขวามาซ้ายไปแสดงบรรทัดละหนึ่งรหัส
Electrical Appliances: E101 E123 E323 E493 E928 E883'''
def split_product_name_id(data_id:str):

    product_name_str, product_id_str = data_id.split(':')
    
    # ตอน .split() ไม่จำเป็นต้องใช้ list(...) 
    # เพราะ split ออกมาจะเป็น list อยู่แล้ว
    # list_product_id = list(product_id_str.split())
    
    # สูตรประหยัดตัวแปร ไป split() ที่ for เลย
    # list_product_id = product_id_str.split()

    print(product_name_str)
    

    #  วิธีที่ 1 list_product_id[::-1]:
    #  วิธีที่ 2 reversed(list_product_id)
    #  หรืออยากประหยัดตัวแปร ก็มา split() ที่ for เลยก็ได้
    for prod_id in reversed(product_id_str.split()):
        print(prod_id)

split_product_name_id('Electrical Appliances: E101 E123 E323 E493 E928 E883')
print('============ End Function ============\n')


'''อ่านสตริงตามด้วยการ split ให้เป็นลิสต์เก็บใน x จากนั้นอ่านสตริงอีกตัวเก็บใน a จงเขียนคำสั่งเพื่อนับและแสดงว่า มีค่าใน a ที่เก็บอยู่ในลิสต์ x กี่ตัว
X Y Z XY XYZ XYZ XY | XYZ'''
def list_compar(x:str, a:str):

    # ไม่ต้อง list(x.split) เพราะ .split เป็น list อยู่แล้ว
    list_x = x.split()

    # count = 0

    # for e in list_x:
    #     if e == a:
    #         count += 1

    # วิธีที่ pythonic ในการนับจำนวน a ใน list_x คือ
    count = list_x.count(a)

    print('a in x =', count)

list_compar('X Y Z XY XYZ XYZ XY', 'XYZ')
print('============ End Function ============\n')


