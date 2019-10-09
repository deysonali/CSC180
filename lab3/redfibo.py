def fibo(n):
    prev_prev=0
    prev=1
    for i in range(0,n):
        newv=prev+prev_prev
        prev_prev = prev
        prev      = newv
    return prev

def fiboL(n):
    prev_prev=0
    prev=1
    accum=[1]
    for i in range(0,n):
        newv=prev+prev_prev
        prev_prev = prev
        prev      = newv
        accum=accum+[newv]
    return accum

def redPro(a,b):
	return a*b

def redfibo(n):
	l=fiboL(n)
	pro=reduce(redPro,l)
	return pro

