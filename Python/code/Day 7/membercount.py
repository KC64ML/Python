# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

check = False

while(not(check)):
    try:
        people = int(input("관람 인원 수를 입력해주세요: "))
        if people <= 0:
            print("관람 인원 수는 양수만 가능합니다")
        else:
            break
    except Exception:
        print("관람 인원 수는 정수만 가능합니다")

print("관람할 인원 수는 %d명입니다" % people)
