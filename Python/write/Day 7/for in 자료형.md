* for문 활용
  * for in 값의 집합자료형
  * dic = {"human" : "사람", "dog" : "강아지", "carrot" : "당근"}
  * oddnums = (1, 3, 5, 7, 9)
  * evennums = [6, 8, 10, 22]
  * str = "Hello goorm!"
  * for i in oddnums:
  * print(i, end = ' ')
  * print()
  * for i in evennums:
  * print(i, end = ' ')
  * print()
  * for i in str :
  * print(i, end = ' ') => H e l l o g o o r m !
  * for key, val in dic.items():
  * print(key, value, end = ' ') => human 사 람 dog 강 아 지 carrot 당 근
  *  
  * for num in [1,2,3,4,5,6,7] :    
  * print(num)    
  * 1
  * 2
  * ~
  * 7
  * for num in [1,2,3,4,5,6,7] :    
  * print(num, end = ',')
  * 1, 2, 3, 4, 5, 6, 7
  * 
  * num1 = [[1,2,3],[4,5,6]]
  * for i, j, k in num1:
  * print(i, j, k)  
  * => 1 2 3
  * => 4 5 6
  * => a b c
  *  
  * fruits = {"apple" : "red", "banana" : "yellow", "grape" : "purple", "melon" : "green"} 
  * for color in fruits.values():    
  * print(color, end = ' ')  => red yellow purple green
  * print() 
  * for fruit in fruits.keys():  
  * print(fruit, end = ' ')    => apple banana grape melon
  * print() 
  * for fruit, color in fruits.items():    
  * print("%s의 색은 %s" %(fruit, color), end = ', ')
  * => apple의 색은 red, banana의 색은 yellow, grape의 색은 purple, melon의 색은 green





