# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def maxFunc(lista):
	max = 0
	for i in range(0,lista.len):
		if max < i:
			max = i
	return max

A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54] 
maxNum = maxFunc(A)
print(maxNum)


