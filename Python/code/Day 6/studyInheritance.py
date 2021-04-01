# 부모 클래스
class Person :
    job = ""
    
    @classmethod
    def greeting(cls) :
        print("안녕하세요 저는",cls.job,"입니다.")
    
    def printAge(self) :
        print(self.age)

# Person 상속
class Student(Person) :
    job = "student"
    
    def __init__(self, age) :
        self.age = age
        
    def printAge(self) :
        print("저의 나이는", self.age, "입니다.")    

# Person 상속
class Professor(Person) :
    job = "professor"   
    
    def __init__(self, age) :
        self.age = age
        
    def printAge(self) :
        print("저의 나이는", self.age, "입니다.") 
   
std = Student(14)
pf = Professor(56)

std.greeting()
std.printAge()

pf.greeting()
pf.printAge()