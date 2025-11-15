def ex04_04_14():
    t = 'ABCabcAABCABAABC'#input()
    count = 0
    pattern = 'ABC'
    for i in range(len(t)):
        if t[i:].startswith(pattern):
            count += 1
    print(count)
ex04_04_14()