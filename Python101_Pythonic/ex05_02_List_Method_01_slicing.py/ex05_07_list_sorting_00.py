'''แบบฝึกหัด 5-7 
ข้อที่ 1 เขียนคำสั่งอ่านชื่อย่อธนาคารจากอินพุตซึ่งเป็นรายการของชื่อคั่นด้วยช่องว่าง 
เช่น SCB BBL KBANK นำมาเก็บแบบลิสต์ในตัวแปร
ชื่อ banks โดยเก็บเรียงจากซ้ายไปขวาในลิสต์ ตามลำดับพจนานุกรม
KTB BBL SCB KBANK TMB'''

def banks_sort_names(name:str):
    banks = name.split()
    print('Unsort:', banks)
    banks.sort()
    print('Sort:', banks)
banks_sort_names(name='KTB BBL SCB KBANK TMB')
print('============ End Function ============\n')

'''แบบฝึกหัด 5-7 
ข้อที่ 2 เขียนคำสั่งอ่านเลขท้ายสามตัวของสลากกินแบ่งที่ถูกรางวัล
จากอินพุต เช่น 323 434 028 นำมาเก็บแบบลิสต์ในตัวแปร
ชื่อ last3 โดยเก็บจากซ้ายไปขวาในลิสต์ เรียงจากมากไปน้อย 394 392 182 405 093'''
def last3_sort(data:str):
    last3 = data.split()
    last3.sort()
    print('lottary last 3:', last3[::-1])

last3_sort(data='394 392 182 405 093')
print('============ End Function ============\n')


'''แบบฝึกหัด 5-7 ข้อที่ 3
เขียนคำสั่งอ่านชื่อย่อธนาคารและราคาหุ้นจากอินพุตในรูปแบบดัง
ตัวอย่าง SCB=132.0, BBL=176.5, KBANK=172.0 เพื่อแสดง
ชื่อธนาคารกับราคาหุ้น (คั่นด้วยช่องว่าง) บรรทัดละธนาคาร 
เรียงตามชื่อธนาคาร ตามพจนานุกรม
KTB=18.9, BBL=176.5, SCB=132.0, KBANK=172.0, TMB=1.8'''

def banks_name_prices(data:str):
    x = data.split(', ')
    x.sort()
    banks = []
    for e in x:
        n, p = e.split('=')
        banks.append([n, float(p)])

    # เขียนแบบ list comp ซ้อน list comp
    banks_list_comp = [ [name, float(price)] for name, price 
                       in [e.split('=') for e in x] ]

    print('For Nomal')
    for n, p in banks:
        print(f'{n:5} {p:>5}')
    print('-'*40)
    print('For Comp')
    for n, p in banks_list_comp:
        print(f'{n:5} {p:>5}')


banks_name_prices(data='KTB=18.9, BBL=176.5, SCB=132.0, KBANK=172.0, TMB=1.8')
print('============ End Function ============\n')


'''เขียนคำสั่งอ่านชื่อย่อธนาคารและราคาหุ้นจากอินพุตในรูปแบบดังตัวอย่าง SCB=132.0, BBL=176.5, KBANK=172.0 เพื่อมาประมวลผลและแสดงชื่อธนาคาร บรรทัดละชื่อ จากชื่อที่มีราคาหุ้นมากสุดมาน้อยสุด
TB=18.9, BBL=176.5, SCB=132.0, KBANK=172.0, TMB=1.8'''

def banks_name_price_max(data:str):
    x = data.split(', ')
    banks = []
    for e in x:
        name, price = e.split('=')
        banks.append([float(price), name])
    
    print('ธนาคารที่มีราคาหุ้นเรียงจากมากสุด')
    banks.sort()
    for no, name in enumerate(banks[::-1]):
        print(no+1, name[1])

banks_name_price_max(data='TB=18.9, BBL=176.5, SCB=132.0, KBANK=172.0, TMB=1.8')
print('============ End Function ============\n')
