import sys
sys.set_int_max_str_digits(0)

'''ฝึกเขียนโจทย์แนวเดียวกัน (ให้ป๋าลอง)
Problem Name (EN): ReverseMultiplyPalindrome
ชื่อโจทย์ (TH): ค้นหาจำนวนที่ไม่เกิดพาลินโดรมจากการกลับเลขแล้วคูณ'''

def reverse_and_multiply(n):
    rev = int(str(n)[::-1])
    return n * rev
# print(reverse_and_multiply(57))

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_lychrel(n):
    current = n
    for _ in range(30):
        current = reverse_and_multiply(current)
        if is_palindrome(current):
            return False
    return True

def find_lychrel_after_N():
    N = int(input())
    candidate = N + 1
    while True:
        if is_lychrel(candidate):
            print(candidate)
            break
        candidate += 1

find_lychrel_after_N()


