# coding: utf-8
def genBoard():
    return [0,0,0,0,0,0,0,0,0]
 
def printBoard(T):
    if len(T) !=9:
        return False
    accum = []
    for i in range(0,len(T),1):
        if T[i]==0:
            accum = accum + [ str(i) ]
        elif T[i]==1:
            accum = accum + [ 'X' ]
        elif T[i]==2:
            accum = accum + [ 'O' ]
        else:
            return False
    print " "+ accum[0]+" | "+accum[1]+" | "+ accum[2]
    print "---|---|---"
    print " "+accum[3]+" | "+accum[4]+" | "+ accum[5]
    print "---|---|---"
    print " "+accum[6]+" | "+accum[7]+" | "+ accum[8]
    return True

def analyzeBoard(T):
         if len(T)!=9:
             return -1
         for i in range(0,len(T),1):
             if(T[i]!=0 and T[i]!=1 and T[i]!=2):
                 return -1
         if(T[0]==T[1]==T[2]==1):
             return 1
         elif(T[3]==T[4]==T[5]==1):
             return 1
         elif(T[6]==T[7]==T[8]==1):
             return 1
         elif(T[0]==T[3]==T[6]==1):
             return 1
         elif(T[2]==T[5]==T[8]==1):
             return 1
         elif(T[1]==T[4]==T[7]==1):
             return 1
         elif(T[0]==T[4]==T[8]==1):
             return 1
         elif(T[2]==T[4]==T[6]==1):
             return 1
         elif(T[0]==T[1]==T[2]==2):
             return 2
         elif(T[3]==T[4]==T[5]==2):
             return 2
         elif(T[6]==T[7]==T[8]==2):
             return 2
         elif(T[0]==T[3]==T[6]==2):
             return 2
         elif(T[2]==T[5]==T[8]==2):
             return 2
         elif(T[1]==T[4]==T[7]==2):
             return 2
         elif(T[0]==T[4]==T[8]==2):
       	     return 2
         elif(T[2]==T[4]==T[6]==2):
             return 2
         elif(T[0]==0 or T[1]==0 or T[2]==0 or T[3]==0 or T[4]==0 or T[5]==0 or T[6]==0 or T[7]==0 or T[8]==0):
             return 0
         else:
             return 3

def genRandomMove(T,player):
         if(player!=1 and player!=2):
             return -1
         elif(len(T)!=9):
             return -1
         for i in range(0,len(T),1):
             if(T[i]!=0 and T[i]!=1 and T[i]!=2):
                 return -1
         if(T[0]!=0 and T[1]!=0 and T[2]!=0 and T[3]!=0 and T[4]!=0 and T[5]!=0 and T[6]!=0 and T[7]!=0 and T[8]!=0):
             return -1
         else:
             while True:
                 move=randint(0,8)
                 if T[move]==0:
                     return move
                     break

def genWinningMove(T,player):
        if(player!=1 and player!=2):
            return -1
        elif(len(T)!=9):
            return -1
        if(T[0]!=0 and T[1]!=0 and T[2]!=0 and T[3]!=0 and T[4]!=0 and T[5]!=0 and T[6]!=0 and T[7]!=0 and T[8]!=0):
            return -1
        for i in range(0,len(T),1):
            if(T[i]!=0 and T[i]!=1 and T[i]!=2):
                return -1
        for i in range(0,9):
            if T[i]==0:
               testboard=list(T)
               testboard[i]=player
               if analyzeBoard(testboard)==player:
                   return i
        else:
            return -1
  

def genNonLoser(T,player):
    if(player!=1 and player!=2):
	return -1
    elif(len(T)!=9):
	return -1
    if(T[0]!=0 and T[1]!=0 and T[2]!=0 and T[3]!=0 and T[4]!=0 and T[5]!=0 and T[6]!=0 and T[7]!=0 and T[8]!=0):
	return -1
    for i in range(0,len(T),1):
	if(T[i]!=0 and T[i]!=1 and T[i]!=2):
	   return -1
    if player==1:
	opponent=2
    else:
	opponent=1
    for i in range(0,9):
	if T[i]==0:
	   testboard=list(T)
	   testboard[i]=opponent
	   if analyzeBoard(testboard)==opponent:
	       return i
    else:
	return -1
	    
