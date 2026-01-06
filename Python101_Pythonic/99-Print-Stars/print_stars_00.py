'''
*****
 *  *
  * *
   **
    *
'''

def stars_01(n:int):
    for row in range(n):
        for col in range(n):
            if row == 0 or row == n:
                print('*', end='')
            else:
                if col == row or col == n-1:
                    print('*', end='')
                else:
                    print(' ', end='')
        print()
stars_01(10)


'''
**********
*        *
**********
*        *
**********
'''
