# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

numbers = [10, 24, 52, 6, 30, 15, 2, 19, 27, 22]

numbers[0:1] = [40]
print(numbers)

numbers[5] = "goorm"
print(numbers)

numbers[2:4] = ['b','i','g']
print(numbers)

del numbers[2:7]
print(numbers)