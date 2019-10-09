from counterlib import counter

a=counter(50)
b=counter(1000)
c=counter(-100)

for i in range(1,21,1): #different counters
	print("Testing a= " +str(a.getState())+" and b= "+ str(b.getState()) +" and c= "+str(c.getState())+" to increment by "+ str(i)+" 5 times")
	for j in range(0,5,1): #test the counter that many times
		print("Run "+str(j))
		a.evolve(i)
		b.evolve(i)
		c.evolve(i)
		print ("a is now "+str(a.getState()))
		print ("b is now "+str(b.getState()))
		print ("c is now "+str(c.getState()))


		
		
