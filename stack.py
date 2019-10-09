class stack:
	def __init__(self):
		self.store=[]

	def push(self, x):

		if(type(x) == int):
			self.store=self.store+[x]
		else:
			return False
	
	def pop(self):
		if (len(self.store)==0):
			return False
		else:
			rval=self.store[len(self.store)-1]
			self.store=self.store[0:len(self.store)-1]
			return rval

	def disp(self):
        	for i in range(0,len(self.store)):
       	                print self.store[i],"<--top--" if i==len(self.store)-1 else ""	
