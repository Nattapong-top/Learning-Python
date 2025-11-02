# โจทย์ที่ 2: หาระยะห่างแบบ Euclideanสถานการณ์: คุณมีจุด 2 จุดใน 3 มิติ 
# (p1 และ p2) ซึ่งเก็บในลิสต์เป้าหมาย: จงหาระยะห่างแบบ Euclidean (Euclidean distance) 
# ระหว่างจุดทั้งสองสูตร: sqrt{(x_1-y_1)^2 + (x_2-y_2)^2 + (x_3-y_3)}

import math

p1 = [55, 66, 77]
p2 = [880000, 990000, 1100000]

sum_of_squares = sum((a - b)**2 for a, b in zip(p1, p2) )
distance = math.sqrt(sum_of_squares)
print(f'ระยะห่างคือ: {distance:,.2f}')


