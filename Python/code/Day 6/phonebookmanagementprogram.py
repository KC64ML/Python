# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

class phoneBook():
    def __init__(self, name, number, residence):
        self.name = name
        self.number = number
        self.residence = residence
    print("info is saved")

    def showData(self):
        print("{2} 거주 {0}: {1}".format(self.name,self.number,self.residence))


class BestFriend(phoneBook):
    def __init__(self, name, number, residence, age, hobby):
        self.name = name
        self.number = number
        self.residence = residence
        self.age = age
        self.hobby = hobby

        print("info is saved")

    def specialData(self):
          print("{0}살, {1}가 취미".format(self.age, self.hobby))


user1 = phoneBook("김구름", "01011111111", "판교")
user1.showData()

friend1 = BestFriend("이에듀", "01022222222", "강남", "23", "영화보기")
friend1.showData()
friend1.specialData()
