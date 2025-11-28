def sort_least(x:list):
    y = False

    for i in range(len(x) -1):
        if x[i] > x[i+1]:
            y = True
            break
    
    if y:
        print('NO')
    else:
        print('YES')

sort_least(x=[1,2,3,8,6,6])