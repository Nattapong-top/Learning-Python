'''แบบฝึกหัด 6-3 ข้อที่ 1
จงเขียนฟังชัน dot ที่รับลิสต์ของจำนวนจริง 2 ลิสต์ 
แต่ละลิสต์แทนเวกเตอร์มีขนาดเท่ากัน ฟังก์ชันนี้คำนวณและคืน
dot product ของสองเวกเตอร์ที่ได้รับ'''

def dot(a:list, b:list):
    return [i*j for i, j in zip(a, b)]

a = [1, 2, 3]
b = [1, 2, 3]
dot_product = dot(a, b)
print(dot_product)

'''แบบฝึกหัด 6-3 ข้อที่ 2
จงเขียนฟังชัน add ที่รับลิสต์ของจำนวนจริง 2 ลิสต์ 
แต่ละลิสต์แทนเวกเตอร์มีขนาดเท่ากัน  
ฟังก์ชันนี้คำนวณและคืนผลบวกของสองเวกเตอร์ที่ได้รับ'''

def add(a:list, b:list):
    return [i+j for i, j in zip(a, b)]

a = [1, 2, 3]
b = [1, 2, 3]
add_list = add(a, b)
print(add_list)


'''จงเขียนฟังชัน to_list_of_strings ที่รับลิสต์หนึ่งตัว 
เพื่อสร้างและคืนลิสต์อีกตัวที่ภายในเก็บค่าที่นำข้อมูลจากลิสต์ที่รับมาแปลงเป็นสตริง 
เช่น รับ [1,2,3] จะคืน ['1', '2', '3']'''

def to_list_of_strings(data:list):
    return [str(c) for c in data]

data = [1, 2, 3]
data_to_str = to_list_of_strings(data)
print(data_to_str)

'''จงเขียนฟังก์ชัน get_positive(x) ฟังก์ชันนี้รับลิสต์ของจำนวน 
เพื่อคืนลิสต์ใหม่ที่เก็บจำนวนใน x เฉพาะตัวที่เป็นจำนวนบวก 
(เก็บเรียงลำดับก่อนหลังเหมือนใน x) เช่น 
x = [0,1,0,-2,9,3-4] จะคืน [1,9,3]'''

def get_positive(x:list):
    return [n for n in x if n > 0]

x = [0, 1, 0, -22, 9, 3, -4, 6]
list_positive = get_positive(x)
print(list_positive)


'''จงเขียนฟังก์ชัน get_peak_indexes(x) ฟังก์ชันนี้รับลิสต์ของจำนวน 
เพื่อหาและคืนอินเด็กซ์ต่าง ๆ ของ x ที่มีข้อมูลที่มากกว่าตัวที่ติดกันทางซ้ายและขวา 
เช่น x = [0,1,9,3,4,99,3,4,6,0,9] จะคืน [2,5,8]'''

def get_peak_indexes(x:list):
    # indexs = []
    # for i in range(1, len(x)-1):
    #     if x[i-1] < x[i] > x[i+1]:
    #         indexs.append(i)

    # return indexs
    return [i for i in range(1, len(x)-1) if x[i-1] < x[i] > x[i+1] ]

x = [0,1,9,3,4,99,3,4,6,0,9]
list_indexs = get_peak_indexes(x)
print(list_indexs)


'''แบบฝึกหัด 6-3 ข้อที่ 6
จงเขียนฟังก์ชัน all_even ที่รับ x เป็นลิสต์ของจำนวนเต็ม ฟังก์ชันนี้คืนจริงถ้าทุกค่าใน 
x เป็นจำนวนคู่ ไม่เช่นนั้นก็คืนเท็จ และเขียนอีกฟังก์ชัน all_even_positions_even 
ที่รับ x เป็นลิสต์ของจำนวนเต็ม ฟังก์ชันนี้คืนจริง ถ้าทุกค่าที่ index คู่ใน x 
เป็นจำนวนคู่ ไม่เช่นนั้นก็คืนเท็จ'''

'''ตัวอย่างโค๊ดแบบมือสมัครเล่น'''
num_x = [2,4,6,7]

# *** ตีโจทย์ คืนจริงถ้าทุกค่าใน x เป็นจำนวนคู่ 
# ในโค๊ดนี้จะเช็คทุกตัวและเก็บผลลัพธ์ไว้แล้วมาเช็คตอนจบอีกทีว่า
# เป็นจริงทั้งหมดหรือเป็นเท็จทั้งหมด ซึ่งก็ถูก แต่ช้ากว่า
# เราสามารถทำให้เร็วขึ้นได้คือ เปลี่ยนจากว่ามีทรูหรือไม่
# ให้เช็คว่ามีเท็จหรือไม่ ถ้ามีเท็จให้รีเทรินเท็จเลย ไม่ต้องเช็คให้ครบทุกตัว
def all_even(x:list):
    even = []
    for n in x:
        if n%2 == 0:
            even.append(True)
        else:
            even.append(False) 
    return all(even)

def all_even_positions_even(x:list):
    # โค๊ดส่วนนี้ เราสามารถ ใช้ silencing ได้
    # num = x[::2] ได้ผลเหมือนกัน แต่สั่นและเร็วกว่า
    num = [x[i] for i in range(0, len(x), 2)]
    even = all_even(num)
    return even

num_even = all_even(num_x)
print(num_even)

num_index_even = all_even_positions_even(num_x)
print('index even', num_index_even)


'''โค๊ดแบบมีอาชีพ'''
# เช็คว่าเป็นเท็จหรือไม่ ถ้าใช้ รีเทรินเท็จ ถ้าทุกตัวเป็นทรู ถึงจะรีเทรินจริง
# ถ้ามีเท็จก็ไม่ต้องเช็คทุกตัว
def all_even_2(x:list):
    for e in x:
        if e%2 == 1:
            return False
    return True

def all_even_position_even_2(x:list):
    # ใช้ silencing [::2] แทน [for e % == 2 นับจำนวณคู่]
    num = x[::2]
    num_index = all_even_2(num)
    return num_index

num_even_2 = all_even_2(num_x)
print('num even 2', num_even_2)

num_index_even_2 = all_even_position_even_2(num_x)
print('num index even 2', num_index_even_2)

    

