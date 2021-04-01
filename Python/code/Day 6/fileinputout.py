# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

A = [1,2,3,9,5,6,4,8,7]
A = sorted(A)
F = open("/data/out.txt",'w')
  
for i in A:
	data = i
	F.write(str(data))
	
  
F.close()