'''แบบฝึกหัด 5-6 
ข้อที่ 1 โปรแกรมข้างล่างนี้อ่านชื่อย่อจังหวัด ไทยกับอังกฤษ คั่นด้วยช่องว่าง 
เช่น BKK กทม CMI ชม KBI กบ นำมาสร้างเป็นลิสต์ eng = ["BKK", "CMI", "KBI"] 
กับลิสต์ th = ["กทม", "ชม", "กบ"] 
จงเขียนคำสั่งต่อที่อ่านชื่อย่อจังหวัดจากอินพุต ถ้าเป็นชื่อย่อไทย 
ก็แสดงชื่อย่ออังกฤษ ถ้าเป็นชื่อย่ออังกฤษก็แสดงชื่อย่อไทย ถ้าไม่ใช่ทั้งสอง ก็แสดง Not found'''
import random

def found_name_th_eng():
    x = 'CBI ชบ BKK กทม CMI ชม KBI กบ KNN ขก'.split()
    eng = x[::2]
    th = x[1::2]

    q = random.choice(['KNN', 'JP', 'กบ'])
    print(q)
    if q in eng:
        print(th[eng.index(q)])
    elif q in th:
        print(eng[th.index(q)])
    else:
        print('Not found')
found_name_th_eng()
print('\n')

'''แบบฝึกหัด 5-6 
ข้อที่ 2 โปรแกรมข้างล่างนี้อ่านชื่อย่อจังหวัด ไทยกับอังกฤษ คั่นด้วยช่องว่าง 
เช่น BKK กทม CMI ชม KBI กบ นำมาสร้างเป็นลิสต์ 
abbr = [["BKK","กทม"], ["CMI","ชม"], ["KBI","กบ"]] 
จงเขียนคำสั่งต่อที่อ่านชื่อย่อจังหวัดจากอินพุต ถ้าเป็นชื่อย่อไทย 
ก็แสดงชื่อย่ออังกฤษ ถ้าเป็นชื่อย่ออังกฤษก็แสดงชื่อย่อไทย ถ้าไม่ใช่ทั้งสอง ก็แสดง Not found'''

def found_name_th_eng_nested_list():
    x = 'CBI ชบ BKK กทม CMI ชม KBI กบ KNN ขก'.split()
    abbr = []
    found = False
    for i in range(0,len(x),2):
        abbr.append([x[i],x[i+1]])

    q = random.choice(['KNN', 'JP', 'กบ'])
    print(q)
    for eng, th in abbr:
        if q == th:
            print(eng)
            found = True
        elif q == eng:
            print(th)
            found = True
    
    if not found:
        print('Not found')

found_name_th_eng_nested_list()
print('\n')
