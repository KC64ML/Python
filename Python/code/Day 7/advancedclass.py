class First:
    name = "first"

    def __init__(self):
        print("First class")

    def printFirst(self):
        print("first")


class Second:
    name = "second"

    def __init__(self):
        print("First class")

    @classmethod
    def printName(cls):
        print(cls.name)


class Third(First, Second):
    pass


third = Third()
third.printName()
third.printFirst()
