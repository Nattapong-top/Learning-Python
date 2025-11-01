# โจทย์ที่ 1: สร้าง Dictionary
# สถานการณ์: คุณมีลิสต์ 2 อัน ลิสต์หนึ่งเก็บ "กุญแจ" (keys) 
# และอีกอันเก็บ "ค่า" (values) ที่สอดคล้องกัน 
# เป้าหมาย: จงสร้าง Dictionary (พจนานุกรม) จากลิสต์ทั้งสองนี้
keys = ['name', 'position', 'salary']
values = ['nattanan', 'IT Support', 20000]

profile = dict(zip(keys, values) )
print(profile)