def if_04(a:int, b:int = 0):
    if a % 2 == 0:
        b = 2 * a
        
        if a > 10:
            a //= 2
        
        else:
            b += a

        a += b
    a *= 2

    return a, b
print('8, 4', if_04(8, 4))
print('112, 41', if_04(112, 41))
print('3, 1', if_04(3, 1))
print('2, 1', if_04(2, 1))