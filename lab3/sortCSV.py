import sys

def genSortKey(col,di):
     def key(x):
         if di=="+":
                return x[col]
         elif di=="-":
                return -x[col]
         else:
                print "Error"

     return key


FIN=""
FOUT=""
Col=0
Dir=""
accum=[]
nargs=len(sys.argv)
skip=False
for i in range(1,nargs):
   if not skip:
      arg=sys.argv[i]
      if arg == "--fin":
         if i != nargs-1:
		FIN=sys.argv[i+1]
                f=open(FIN,'r')
		lines=f.readlines()
		f.close()		
		for i in lines:
   			j=i.split('\n')[0]  
   			k=j.split(',')      
   			r=[]
  		        for x in k:
     		            r = r + [float(x)]
  		        accum = accum + [r] 
	    		
      		skip=True
      elif arg == "--fout":
	if i != nargs-1:
            FOUT=sys.argv[i+1]
            skip=True

      elif arg == "--col":
	  if i != nargs-1:   
	  
		try:  
	 	    	Col=int(sys.argv[i+1])
			
    
		except:
			print "Error: Illegal Choice"
		skip=True

      elif arg == "--dir":
	 if i != nargs-1:
            Dir=sys.argv[i+1]
            skip=True
		
      else:
         print "ERR: unknown arg:",arg
   else:
      skip=False

length=len(accum[0])
if (Col>=0 and Col<length):
	sortKey=genSortKey(Col,Dir)
	sortedlist=sorted(accum,key=sortKey)
	
	try:
		g=open(FOUT,'w')
		for i in range (0,len(sortedlist)):
			com=(str(sortedlist[i])).split('[')[1]
			com2=(com).split(']')[0]
			g.write(com2+'\n')
		g.close()
	
	except:
		print "Error creating file"
else:

	print "Column not legal"

