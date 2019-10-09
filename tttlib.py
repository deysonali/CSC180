
#Sonali Dey
from random import randint

class ttt:
	def __init__(self):
		self.T=[0,0,0,0,0,0,0,0,0]
	def copy(self,source):
		for i in range(0,len(self.T)):
			self.T[i]=source[i]
	 
	def printBoard(self):
	    if len(self.T) !=9:
		return False
	    accum = []
	    for i in range(0,len(self.T),1):
		if self.T[i]==0:
		    accum = accum + [ str(i) ]
		elif self.T[i]==1:
		    accum = accum + [ 'X' ]
		elif self.T[i]==2:
		    accum = accum + [ 'O' ]
		else:
		    return False
	    print " "+ accum[0]+" | "+accum[1]+" | "+ accum[2]
	    print "---|---|---"
	    print " "+accum[3]+" | "+accum[4]+" | "+ accum[5]
	    print "---|---|---"
	    print " "+accum[6]+" | "+accum[7]+" | "+ accum[8]
	    return True

	def analyzeBoard(self):
		 if len(self.T)!=9:
		     return -1
		 for i in range(0,len(self.T),1):
		     if(self.T[i]!=0 and self.T[i]!=1 and self.T[i]!=2):
			 return -1
		 if(self.T[0]==self.T[1]==self.T[2]==1):
		     return 1
		 elif(self.T[3]==self.T[4]==self.T[5]==1):
		     return 1
		 elif(self.T[6]==self.T[7]==self.T[8]==1):
		     return 1
		 elif(self.T[0]==self.T[3]==self.T[6]==1):
		     return 1
		 elif(self.T[2]==self.T[5]==self.T[8]==1):
		     return 1
		 elif(self.T[1]==self.T[4]==self.T[7]==1):
		     return 1
		 elif(self.T[0]==self.T[4]==self.T[8]==1):
		     return 1
		 elif(self.T[2]==self.T[4]==self.T[6]==1):
		     return 1
		 elif(self.T[0]==self.T[1]==self.T[2]==2):
		     return 2
		 elif(self.T[3]==self.T[4]==self.T[5]==2):
		     return 2
		 elif(self.T[6]==self.T[7]==self.T[8]==2):
		     return 2
		 elif(self.T[0]==self.T[3]==self.T[6]==2):
		     return 2
		 elif(self.T[2]==self.T[5]==self.T[8]==2):
		     return 2
		 elif(self.T[1]==self.T[4]==self.T[7]==2):
		     return 2
		 elif(self.T[0]==self.T[4]==self.T[8]==2):
		     return 2
		 elif(self.T[2]==self.T[4]==self.T[6]==2):
		     return 2
		 elif(self.T[0]==0 or self.T[1]==0 or self.T[2]==0 or self.T[3]==0 or self.T[4]==0 or self.T[5]==0 or self.T[6]==0 or self.T[7]==0 or self.T[8]==0):
		     return 0
		 else:
		     return 3

	def genRandomMove(self,player):
		 if(player!=1 and player!=2):
		     return -1
		 elif(len(self.T)!=9):
		     return -1
		 for i in range(0,len(self.T),1):
		     if(self.T[i]!=0 and self.T[i]!=1 and self.T[i]!=2):
			 return -1
		 if(self.T[0]!=0 and self.T[1]!=0 and self.T[2]!=0 and self.T[3]!=0 and self.T[4]!=0 and self.T[5]!=0 and self.T[6]!=0 and self.T[7]!=0 and self.T[8]!=0):
		     return -1
		 else:
		     while True:
			 move=randint(0,8)
			 if self.T[move]==0:
			     return move
			     break

	def genWinningMove(self,player):
		if(player!=1 and player!=2):
		    return -1
		elif(len(self.T)!=9):
		    return -1
		if(self.T[0]!=0 and self.T[1]!=0 and self.T[2]!=0 and self.T[3]!=0 and self.T[4]!=0 and self.T[5]!=0 and self.T[6]!=0 and self.T[7]!=0 and self.T[8]!=0):
		    return -1
		for i in range(0,len(self.T),1):
		    if(self.T[i]!=0 and self.T[i]!=1 and self.T[i]!=2):
			return -1
		for i in range(0,9):
		    if self.T[i]==0:
                       test=ttt()
                       test.copy(self.T)
                       test.Move(i,player)
                       if test.analyzeBoard()==player:
		      	   return i
		else:
		    return -1
	  

       	def genNonLoser(self,player):
	    if(player!=1 and player!=2):
		return -1
	    elif(len(self.T)!=9):
		return -1
	    if(self.T[0]!=0 and self.T[1]!=0 and self.T[2]!=0 and self.T[3]!=0 and self.T[4]!=0 and self.T[5]!=0 and self.T[6]!=0 and self.T[7]!=0 and self.T[8]!=0):
		return -1
	    for i in range(0,len(self.T),1):
		if(self.T[i]!=0 and self.T[i]!=1 and self.T[i]!=2):
		   return -1
	    if player==1:
		opponent=2
	    else:
		opponent=1
	    for i in range(0,9):
		if self.T[i]==0:
		   test=ttt()
		   test.copy(self.T)	
		   test.Move(i,opponent)
		   if test.analyzeBoard()==opponent:
		       return i
	    else:
		return -1

        def Move(self,x,player):
            if(player!=1 and player!=2):
	  	  return False
	    if x not in range (0,9):
		  return False
	    else:
		  if self.T[x]==0:
			 self.T[x]=player
			 return True
		  else:
			 return False
	  
