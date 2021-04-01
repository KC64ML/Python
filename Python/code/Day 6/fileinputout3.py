# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

f = open("data/add.txt",'w')
name = input("당신의 이름은 무엇입니까?\n")
f.write(str(name))
f.close()

a = open("data/add.txt",'r')
for x in a:
	print(x)

a.close()

