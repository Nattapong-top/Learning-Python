def ex04_04_14():
    t = 'ABCabcAABCABAABC'

    count = 0
    for i, v in enumerate(t,1):
        if v[i:i+3] == 'ABC':
            count += 1
    print(count)
ex04_04_14()