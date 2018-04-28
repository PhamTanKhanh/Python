class HCN:
	ten=""
	dai=0
	rong=0

	def __init__(self,ten,dai,rong):
		self.ten=ten
		self.dai=dai
		self.rong=rong
	
	def toString(self):
		return "HCN" + str(self.ten) + "["+ str(self.dai) +","+ str(self.rong) + "]"	
	
	def getCV(self):
		return (self.dai+self.rong)*2
	
	def getDT(self):
		return self.dai*self.rong
	
	
