'''==============================
Practice Set: Loop & Nested Loop
ชุดฝึก: วนซ้ำและวนซ้อน
==============================

--------------------------------
[BASIC LEVEL] (5 Problems)
--------------------------------

1) Problem Name (EN): CountLines
   ชื่อโจทย์ (TH): นับจำนวนบรรทัด

   Description:
   รับข้อความทีละบรรทัด
   หยุดเมื่อผู้ใช้พิมพ์ END
   ให้นับว่ามีทั้งหมดกี่บรรทัด (ไม่รวม END)

   Function Name:
   count_lines()

   Test Case:
   Input:
   hello
   world
   python
   END

   Output:
   3

'''
def count_lines():
   count = 0
   while True:
      line = input('nums ("END" stop)')
      if not line:
            continue
      elif line.upper() == 'END':
            break
      else:
            count += 1
   return count

# print(count_line())


'''
--------------------------------

2) Problem Name (EN): SumNumbersInLine
   ชื่อโจทย์ (TH): หาผลรวมตัวเลขในบรรทัดเดียว

   Description:
   รับตัวเลขหลายตัวใน 1 บรรทัด (คั่นด้วยช่องว่าง)
   ให้วน loop เพื่อหาผลรวมทั้งหมด

   Function Name:
   sum_numbers_in_line()

   Test Case:
   Input:
   10 20 30 5

   Output:
   65
'''
def sum_numbers_in_line():
     total = 0
     line = input('nums: ')
     
     parts = line.split()
     for num in parts:
          if num.lstrip('-').isdigit():
            total += int(num)
     return total
# print(sum_numbers_in_line())



'''
--------------------------------

3) Problem Name (EN): CountPositiveNumbers
   ชื่อโจทย์ (TH): นับจำนวนเลขบวก

   Description:
   รับตัวเลขทีละบรรทัด
   หยุดเมื่อพิมพ์ END
   ให้นับเฉพาะตัวเลขที่มากกว่า 0

   Function Name:
   count_positive_numbers()

   Test Case:
   Input:
   5
   -2
   8
   0
   -1
   END

   Output:
   2

'''
def count_positive_numbers():
   total = 0
   while True:
      nums = input('nums ("END" stop): ')
      if nums.upper() == 'END':
           break
      elif nums.lstrip('-').isdigit():
           if int(nums) > 0:
               total += 1
   return total
# print(count_positive_numbers())


'''
--------------------------------

4) Problem Name (EN): PrintSquareStars
   ชื่อโจทย์ (TH): พิมพ์ดาวเป็นสี่เหลี่ยม

   Description:
   รับเลข n
   พิมพ์ดาว (*) เป็นรูปสี่เหลี่ยม n x n
   ใช้ nested loop เท่านั้น

   Function Name:
   print_square_stars(n)

   Test Case:
   Input:
   3

   Output:
   ***
   ***
   ***
'''
def print_square_stars(n:int):
     for row in range(n):
          for star in range(n):
               print('*', end='')
          print()
# print_square_stars(5)


'''
--------------------------------

5) Problem Name (EN): CountCharacters
   ชื่อโจทย์ (TH): นับจำนวนตัวอักษรทั้งหมด

   Description:
   รับข้อความหลายบรรทัด
   หยุดเมื่อพิมพ์ END
   ให้นับจำนวนตัวอักษรทั้งหมด (ไม่รวมช่องว่าง)

   Function Name:
   count_characters()

   Test Case:
   Input:
   hi
   python
   END

   Output:
   8
'''

def count_characters():
      count = 0
      while True:
         line = input('input ("END" stop): ')
         if line.upper() == 'END':
              break
         for ch in range(len(line)):
              count += 1
      return count
# print(count_characters())

'''
--------------------------------
[UP LEVEL] (5 Problems)
--------------------------------

6) Problem Name (EN): CountAllNumbers
   ชื่อโจทย์ (TH): นับจำนวนตัวเลขทั้งหมด

   Description:
   รับข้อมูลทีละบรรทัด
   แต่ละบรรทัดมีตัวเลขได้หลายตัว
   หยุดเมื่อพิมพ์ END
   ให้นับว่ามีตัวเลขทั้งหมดกี่ตัว
   (ใช้ nested while)

   Function Name:
   count_all_numbers()

   Test Case:
   Input:
   1 2 3
   4 5
   6
   END

   Output:
   6
'''
def count_all_numbers():
     count = 0
     while True:
          line = input('nums ("END" stop): ')
          if line.upper() == "END":
               break
          elif not line:
               continue
          else:
               nums = line.split()
               for num in nums:
                  if num.lstrip('-').isdigit():
                        count += 1
     return count
# print(count_all_numbers())

'''
--------------------------------
7) Problem Name (EN): MaxNumberFromInput
   ชื่อโจทย์ (TH): หาเลขมากที่สุดจากข้อมูลหลายบรรทัด

   Description:
   รับตัวเลขหลายบรรทัด
   แต่ละบรรทัดมีหลายตัว
   หยุดเมื่อพิมพ์ END
   ให้หาเลขที่มีค่ามากที่สุด

   Function Name:
   max_number_from_input()

   Test Case:
   Input:
   3 9 1
   4 15 2
   7
   END

   Output:
   15
'''

def max_number_from_input():
     max_num = None
     while True:
         line = input('7. input ("END"): ')
         if line.upper() == 'END':
              break
         if not line:
              continue
         parst = line.split()
         count = 0
         while count < len(parst):
              num_str = parst[count]
              if num_str.lstrip('-').isdigit():
                   num = int(num_str)
                   if max_num is None or max_num < num:
                        max_num = num
              count += 1
     return max_num
print(max_number_from_input())

'''
--------------------------------

8) Problem Name (EN): PrintRightTriangle
   ชื่อโจทย์ (TH): พิมพ์สามเหลี่ยมมุมฉาก

   Description:
   รับเลข n
   พิมพ์ดาวเป็นรูปสามเหลี่ยมมุมฉาก
   ความสูง n
   ใช้ nested loop

   Function Name:
   print_right_triangle(n)

   Test Case:
   Input:
   4

   Output:
   *
   **
   ***
   ****
'''
def print_right_triangle(n:int):
     for i in range(1,n+1):
          for j in range(i):
               print('*', end='')
          print()
# print_right_triangle(6)

'''
--------------------------------

9) Problem Name (EN): CountEvenOdd
   ชื่อโจทย์ (TH): นับเลขคู่และเลขคี่

   Description:
   รับตัวเลขหลายบรรทัด
   หยุดเมื่อพิมพ์ END
   ให้นับจำนวนเลขคู่ และเลขคี่

   Function Name:
   count_even_odd()

   Test Case:
   Input:
   1 2 3
   4 5
   END

   Output:
   Even: 2
   Odd: 3
'''
def count_even_odd():
     even = 0
     odd = 0
     
     while True:
          lines = input('9. input nums (END): ')
          if lines.upper() == 'END':
               break
          elif not lines:
               continue
          parts = lines.split()

          for m in parts:
               if m.lstrip('-').isdigit():
                    num = int(m)
                    if num % 2 == 0:
                         even += 1
                    else:
                         odd += 1
     return even, odd
# even, odd = count_even_odd()
# print(f'even:{even}, odd:{odd}')
                         



'''

--------------------------------

10) Problem Name (EN): PrintNumberGrid
    ชื่อโจทย์ (TH): ตารางตัวเลขเพิ่มค่า

    Description:
    รับเลข n
    พิมพ์ตาราง n x n
    ตัวเลขเริ่มจาก 1 เพิ่มทีละ 1 เรียงซ้ายไปขวา บนลงล่าง

    Function Name:
    print_number_grid(n)

    Test Case:
    Input:
    3

    Output:
    1 2 3
    4 5 6
    7 8 9
'''
def print_number_grid(n:int):
     count = 1
     for row in range(1,n+1):
          for col in range(1,n+1):
               print(count, end=' ')
               count += 1
          print()
# print_number_grid(9)


'''
==============================
END OF PRACTICE SET
==============================
'''