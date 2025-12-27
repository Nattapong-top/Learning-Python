import builtins  # <--- ต้องมีบรรทัดนี้สำคัญที่สุด!

_input_iter = None

def set_input(data):
    """ฟังก์ชันสำหรับป้อนข้อมูลจำลอง"""
    global _input_iter
    lines = data.strip().splitlines()
    _input_iter = iter(lines)

def input(prompt=""):
    """ฟังก์ชัน input ปลอมที่จะดึงค่าจากข้อมูลจำลอง"""
    global _input_iter
    if _input_iter:
        try:
            val = next(_input_iter).strip()
            print(f"{prompt}{val}") 
            return val
        except StopIteration:
            # ถ้าข้อมูลจำลองหมด ให้กลับไปใช้คีย์บอร์ดจริง (ป้องกัน Error)
            _input_iter = None
            return builtins.input(prompt)
    else:
        # ถ้าไม่มีข้อมูลจำลอง ให้ใช้คีย์บอร์ดจริงผ่าน builtins
        return builtins.input(prompt)