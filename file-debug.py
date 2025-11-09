def final_check():
    amount = 5000
    balance = 3000
    is_verified = False

    check_trans = amount > balance or not is_verified
    print(check_trans)
final_check()