# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

class Member:	
	def setId(self,id,password):
         self.id = id
         self.password = password
		
		
		
	def getId(self):
         print(self.id, self.password)
		
		
		
mem1 = Member()
mem1.setId("goorm","goorm1")
mem1.getId()