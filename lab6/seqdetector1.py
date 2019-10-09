class seqdetector:

	def __init__(self):
		self.seq=[]
		self.testlist=["here", "are", "the", "solutions", "to", "the", "next", "exam"]
		self.count=0
	def evolve(self, word):
		det=False
		self.seq = self.seq + [word]
		i=len(self.seq)-1
		if (self.seq[i]==self.testlist[self.count]):
			self.count=self.count+1
		else:
			count=0
	
		if self.count==8:
			self.count=0
			det=True
		return det




		
