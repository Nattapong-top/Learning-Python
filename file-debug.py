def input_num_n():
    n = int(input())
    total_sum = 0
    
    while n > 0:
        #total_sum += n

        if n > 0:
            total_sum += n
        n = int(input('ป้อนตัวเลข: '))

    print(f'ผลรวม: {total_sum}')
input_num_n()