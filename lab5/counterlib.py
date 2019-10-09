class counter:
  	def __init__(self,initCnt):
		self.cnt = initCnt
		
	
	def evolve(self,x):
		if(type(x) == int):
			self.cnt=self.cnt+x
			return True
		else:
			return False
	def getState(self):
		return self.cnt
	
