import tkinter as tk
from tkinter import messagebox

def say_hello():
    # ฟังก์ชันที่จะทำงานเมื่อกดปุ่ม
    messagebox.showinfo("ทักทาย", "สวัสดีครับป๋า! นี่คือ GUI แรกของคุณ")

# 1. สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("โปรแกรม POS ของป๋า")
window.geometry("300x200") # ขนาดกว้างxสูง

# 2. สร้างป้ายข้อความ (Label)
label = tk.Label(window, text="ยินดีต้อนรับสู่ร้านชานม", font=("Arial", 14))
label.pack(pady=20)

# 3. สร้างปุ่มกด (Button)
btn = tk.Button(window, text="คลิกที่นี่", command=say_hello) # command คือสั่งให้ไปเรียกฟังก์ชัน
btn.pack()

# 4. รันโปรแกรมค้างไว้ (คล้าย while True)
window.mainloop()