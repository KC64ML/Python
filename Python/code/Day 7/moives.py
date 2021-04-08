# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

movies = ["Dark Knight", "Harry Porter", "Parasite", "Matrix", "La La Land"]

print()
print("===========영화 목록===========")
for movie in movies:
    print(movie)
print("==============================")
	
choice = input("예매하실 영화를 선택해주세요: ")

# A not in B 구문은 B에 A가 포함되지 않은 경우일 때 사용합니다
while choice not in movies:
	print("예매할 수 없는 영화입니다")
	choice = input("예매하실 영화를 선택해주세요: ")
	
print("%s를 선택하셨습니다" %choice)