'''✅ สรุปสั้นที่สุด
จุด = (x[i], y[i])'''
# ระยะ = (𝑥[𝑖]−𝑥[𝑗])2+(𝑦[𝑖]−𝑦[𝑗])2​
# แกนต้องตรงกันเสมอ

def culcalate_distance(x1, x2, y1, y2):
    return round(((x1-x2)**2 + (y1-y2)**2) ** 0.5,2)

def culcalate_min_distance(raw_a:list, raw_b:list) -> tuple:
    distance = 0
    min_distance = None

    if not raw_a or not raw_b:
        return 0
    elif len(raw_a) != len(raw_b) or len(raw_a) < 2:
        return None # ให้ return type สม่ำเสมอ หรือ raise error
    else:
        for i in range(len(raw_a)):
            for j in range(i+1,len(raw_b)):
                x1 = raw_a[i]
                y1 = raw_b[i]

                x2 = raw_a[j]
                y2 = raw_b[j]

                distance = culcalate_distance(x1, y1, x2, y2)
                
                if min_distance is None or distance < min_distance:
                    min_distance = distance
                    x = x1, y1
                    y = x2, y2
    return x, y, min_distance

raw_a = [0,9,9]
raw_b = [0,9,8]
print(culcalate_min_distance(raw_a, raw_b))

