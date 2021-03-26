# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


sum = 0
def myfunc():

	global sum

	for num in range(0,5):
		value = int(input())
		sum += value
		
	print(sum)


myfunc()
