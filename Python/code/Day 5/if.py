# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54]
odd = 0
even = 0

for i in A:
    if (i%2) :
        odd += 1
    elif (i%2 == 0):
        even += 1
        
print(odd, even)
