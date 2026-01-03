

def max_duplicate_numbers(raw_list:list):
    counter = {}
    max_duplicate = None
    result = None
    if not raw_list:
        return 0
    
    for key in raw_list:
        if str(key).lstrip('-').isdigit():
            num = int(key)
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
    
    for k, v in counter.items():
        if max_duplicate is None or v > max_duplicate:
            max_duplicate = v
            result = k

    return result, max_duplicate, counter

raw_list = [1,1,1,2,2,2,3,3,3,1,1,1,2,'er',-4, '111']
print(max_duplicate_numbers(raw_list))

