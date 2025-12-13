# ก๊อปปี้โค้ดนี้ไปวางได้เลยครับ (มีโจทย์ครบในตัว)

'''ชุดข้อมูลจำลอง (HTML Source Code)'''
html_source = """
<!DOCTYPE html>
<html>
<head>
    <title>ร้านกาแฟป๋าณัฐ (Paa Nat Coffee)</title>
</head>
<body>
    <div class="product">
        <h1>เมนูแนะนำ: เอสเพรสโซ่เย็น</h1>
        <img src="https://paa-shop.com/img/espresso.jpg" alt="Espresso">
        <span class="price">Price: 55 Baht</span>
        <p class="desc"><b>รายละเอียด:</b> เข้มข้น ถึงใจ ตาสว่างยันเช้า</p>
        <a href="https://paa-shop.com/buy/12345">คลิกสั่งซื้อทันที</a>
    </div>
</body>
</html>
"""

'''------------------------------------------
ข้อที่ 1: ดึงหัวข้อเว็บ (Get Title)
โจทย์: จงดึงข้อความที่อยู่ในแท็ก <title> ... </title> ออกมา
เป้าหมาย: ร้านกาแฟป๋าณัฐ (Paa Nat Coffee)
Hint: หาตำแหน่ง > ของแท็กเปิด และ < ของแท็กปิด
------------------------------------------'''
def get_title(html):
    start_tag = "<title>"
    end_tag = "</title>"
    
    # 1. หาตำแหน่งเริ่มต้น (และขยับไปหลัง tag)
    start_index = html.find(start_tag) + len(start_tag)
    
    # 2. หาตำแหน่งสิ้นสุด
    end_index = html.find(end_tag)
    
    # 3. ตัดออกมา
    title = html[start_index:end_index]
    return title

print(f"Title: {get_title(html_source)}")
print('\n')


'''------------------------------------------
ข้อที่ 2: ดึงลิงก์รูปภาพ (Get Image URL)
โจทย์: จงดึง URL ที่อยู่ใน src="..." ของแท็ก <img>
เป้าหมาย: https://paa-shop.com/img/espresso.jpg
Hint: หาคำว่า src=" ก่อน แล้วค่อยหาเครื่องหมาย " ตัวถัดไป
------------------------------------------'''
def get_image_src(html:str):
    # เขียนโค้ดเอง (ลองเลียนแบบข้อ 1)
    # 1. หาตำแหน่ง start (หลังคำว่า src=")
    start_tag = '<img src="'
    stop_tag = '"'
    # 2. หาตำแหน่ง end (เครื่องหมาย " ตัวถัดไป)
    start_index = html.find(start_tag) + len(start_tag)
    stop_index = html.find(stop_tag, start_index)

    url_img = html[start_index:stop_index]

    return url_img

print(f"Image: {get_image_src(html_source)}")
print('\n')


'''------------------------------------------
ข้อที่ 3: ดึงราคาสินค้า (Get Price)
โจทย์: จงดึง "ตัวเลขราคา" (55) ออกมาจากบรรทัด <span class="price">Price: 55 Baht</span>
Hint: หาคำว่า "Price: " แล้วตัดเอาเฉพาะตัวเลข 
(อาจจะต้องใช้ .find() หาตำแหน่งเริ่ม แล้ว slice ไปอีกนิด หรือใช้ .split() ช่วย)
------------------------------------------'''
def get_price(html:str):
    # เขียนโค้ด
    taget = 'Price:'
    start_index = html.find(taget)

    value_start = start_index + len(taget)

    stop_index = html.find('Baht', value_start)

    raw_price = html[value_start:stop_index]

    return raw_price.strip()

print(f"Price: {get_price(html_source)}")
print('\n')


'''------------------------------------------
ข้อที่ 4: ดึงคำอธิบาย (Clean Description)
โจทย์: ดึงข้อความใน <p class="desc"> ออกมา แต่ **ไม่เอา** คำว่า <b>รายละเอียด:</b>
เป้าหมาย: เข้มข้น ถึงใจ ตาสว่างยันเช้า
Hint: เริ่มตัดหลังจาก </b> จนถึง </p>
------------------------------------------'''
def get_description(html:str):
    # หาตำแหน่งปิดของ </b>
    start = '</b>'
    # ตัดตั้งแต่ตรงนั้น จนถึง </p>
    stop = '</p>'

    start_index = html.find(start) + len(start)
    stop_index = html.find(stop)

    desc = html[start_index:stop_index]
    return desc

print(f"Desc: {get_description(html_source)}")
print('\n')


'''------------------------------------------
ข้อที่ 5: ดึง Link สั่งซื้อ (Get Link)
โจทย์: ดึง URL จาก href="..." ในบรรทัด <a>
เป้าหมาย: https://paa-shop.com/buy/12345
Hint: คล้ายๆ ข้อดึงรูปภาพ (src)
------------------------------------------'''
def get_buy_link(html:str):
    # คล้ายๆ ข้อดึงรูปภาพ (src)
    start = 'href="'
    stop = '">'
    index_start = html.find(start) + len(start)
    index_stop = html.find(stop, index_start)
    link = html[index_start:index_stop]
    return link
print(f"Link: {get_buy_link(html_source)}")
print('\n')