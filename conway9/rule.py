def rule(value, l):
	length = len(l)
	sum = 0
	for i in range (0,length):
		sum = sum+l[i]
	if (value==1):
		if(sum==2 or sum==3):
			return 1
		else:
			return 0
	else:
		if(sum ==3):
			return 1
		else:
			return 0

