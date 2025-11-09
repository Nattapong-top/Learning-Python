def scores():
    score1 = (95, 120)
    score2 = (95, 110)
    
    check1 = score2[0] > score1[0]
    
    check2 = (score2[0] == score1[0]) and score2[1] < score1[1]
    
    print(check1 or check2)
scores()