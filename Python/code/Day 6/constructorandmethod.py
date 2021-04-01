# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

class Member:

    def __init__(self, id, password):
        self.id = id
        self.password = password

    def getId(self):
        return self.id +" " + self.password


user1 = Member('goormedu', 'goorm')
print(user1.getId())
