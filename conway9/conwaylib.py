import random
from rule import rule

class conway:
	def __init__(self,a,b,word):
		self.store=[]
		self.next=[]
		self.a = a
		self.b = b
		if word == 'zeros':
			self.store = [[0 for j in range(b)] for i in range(a)]
		if word == 'random':
			self.store = [[random.randint(0,1) for j in range(b)] for i in range(a)]
		
	def getDisp(self):
		str = ''
		for i in range (0, len(self.store)):
			for j in range (0, len(self.store[i])):
				if(self.store[i][j] == 0):
					str = str + " "
				elif(self.store[i][j] == 1):
					str = str + "*"
			str = str + "\n"
		return str
	def printDisp(self):
		print self.getDisp()
		return True
	def setPos(self,row,col,val):
		if((val!=0) and (val!=1)):
			return False
		self.store[row][col]=val
		return True

	def getNeighbours(self,row,col):
		rmax = len(self.store)-1
		cmax = len(self.store[0])-1
		list = []
		if(row==0 and col==cmax):
			list = list + [self.store[rmax][col-1]]+[self.store[rmax][col]]+[self.store[rmax][0]]+[self.store[row][col-1]]+[self.store[row][0]]+[self.store[row+1][col-1]]+[self.store[row+1][col]]+[self.store[row+1][0]]

		elif(row==0 and col==0):
                        list = list + [self.store[rmax][cmax]]+[self.store[rmax][col]]+[self.store[rmax][col+1]]+[self.store[row][cmax]]+[self.store[row][col+1]]+[self.store[row+1][cmax]]+[self.store[row+1][col]]+[self.store[row+1][col+1]]
		elif(row==rmax and col==0 ):
			list = list + [self.store[row-1][cmax]]+[self.store[row-1][col]]+[self.store[row-1][col+1]]+[self.store[row][cmax]]+[self.store[row][col+1]]+[self.store[0][cmax]]+[self.store[0][col]]+[self.store[0][col+1]]
		elif(row==rmax and col==cmax):
			list = list + [self.store[row-1][col-1]]+[self.store[row-1][col]]+[self.store[row-1][0]]+[self.store[row][col-1]]+[self.store[row][0]]+[self.store[0][col-1]]+[self.store[0][col]]+[self.store[0][0]]
		elif(row==0):
			list = list + [self.store[rmax][col-1]]+[self.store[rmax][col]]+[self.store[rmax][col+1]]+[self.store[row][col-1]]+[self.store[row][col+1]]+[self.store[row+1][col-1]]+[self.store[row+1][col]]+[self.store[row+1][col+1]]
		elif(row==rmax):
			list = list + [self.store[row-1][col-1]]+[self.store[row-1][col]]+[self.store[row-1][col+1]]+[self.store[row][col-1]]+[self.store[row][col+1]]+[self.store[0][col-1]]+[self.store[0][col]]+[self.store[0][col+1]]
		elif(col==0):
			list = list + [self.store[row-1][cmax]]+[self.store[row-1][col]]+[self.store[row-1][col+1]]+[self.store[row][cmax]]+[self.store[row][col+1]]+[self.store[row+1][cmax]]+[self.store[row+1][col]]+[self.store[row+1][col+1]]
		elif(col==cmax):
			list = list + [self.store[row-1][col-1]]+[self.store[row-1][col]]+[self.store[row-1][0]]+[self.store[row][col-1]]+[self.store[row][0]]+[self.store[row+1][col-1]]+[self.store[row+1][col]]+[self.store[row+1][0]]
		else:
 			list = list + [self.store[row-1][col-1]]+[self.store[row-1][col]]+[self.store[row-1][col+1]]+[self.store[row][col-1]]+[self.store[row][col+1]]+[self.store[row+1][col-1]]+[self.store[row+1][col]]+[self.store[row+1][col+1]]
		return list

	def evolve(self, rule):
		self.next = [[0 for j in range(self.b)] for i in range(self.a)]
		for i in range(0, len(self.store)):
			for j in range(0, len(self.store[i])):
				self.next[i][j]=rule(self.store[i][j],self.getNeighbours(i,j))
		self.store=self.next
