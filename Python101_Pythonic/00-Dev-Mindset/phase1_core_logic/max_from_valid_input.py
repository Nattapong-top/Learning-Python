# รับลิสต์ตัวเลข หาว่า “ตัวเลขที่มากที่สุด” คืออะไร
def max_from_valid_input(nums_list:list):
    max_value = None
    for n in nums_list:
        if str(n).lstrip('-').isdigit():
            if max_value is None or n > max_value:
                max_value = n
    return max_value

nums_list = [12, 34, -3 , 'er', 34.34, 'error']
print(max_from_valid_input(nums_list))