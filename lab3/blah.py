def fib(a):
	oldest=0
	old=1
	if(a<=0):
		return 0
	elif(a==1):
		return 1
	else:
		for i in range(0,a-1):
			new=oldest+old
			oldest=old
			old=new
		return new

for i in range(1,11):
	print fib(i)


