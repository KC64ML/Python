# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

A = []
F = open("test.txt",'r')

for i in F :
    temp = int(i)  
    A.append(temp)

print(A)

F.close()