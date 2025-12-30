'''แบบฝึกหัด 9-2 ข้อที่ 1
จงเขียนโปรแกรมอ่านรายการของชื่อโรงเรียน เพื่อแสดงรายการการแข่งขันฟุตบอลแบบพบกันหมด 
โดยแสดงบรรทัดละคู่ (เรียงตามพจนานุกรม) ดูตัวอย่างในรูปประกอบ'''

def foob_ball_match_schedule(schools:str):
    teams = schools.split()
    teams.sort()

    for first in range(len(teams)):
        print(teams[first], end=' ')
        for last in range(first+1, len(teams)):
            print(teams[first], end=' ')
foob_ball_match_schedule('BCC AC DS SK')

