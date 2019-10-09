# coding: utf-8
def Palindromize(word):
    accum=word
    for i in range(len(word)-2,-1,-1):
        accum=accum+word[i]
    return accum

def Power(x,n):
    a=1
    if(n==0):
        return a
    elif(n>0):
        for i in range(0,n,1):
            a=a*x
            return a
    else:
        for i in range(0,n,-1):
            a=a*(1.0/x)
            return a

def babylonSqrt(x,accuracy):
    estimate=x/2.0
    while(abs(estimate*estimate-x)>accuracy):
        estimate=0.5((estimate+x)/estimate)
    return estimate


def GCD(a,b):
    if(a<b):
        c=a
        a=b
        b=c
    g=b
    while(a%b!=0):
        g=a%b
        a=b
        b=g
    return g
GCD(9,10)



LeibnizPi(100)
def LeibnizPi(n):
    Neg=True
    a=0.0
    for i in range(1,n+1,1):
        if (Neg==True):
            a=a-(1.0/((2.0*i)+1.0))
            Neg=False
        elif (Neg==False):
            a=a+(1.0/((2.0*i)+1.0))
            Neg=True
    return 4*(a+1)

n=1
while((LeibnizPi(n)-3.14159265>0.01):
    n=n+1
print n,"is the value that gives 0.01 accuracy"

save labn=1
    ...: while((LeibnizPi(n)-3.14159265>0.01):
    ...:     n=n+1
    ...: print n,"is the value that gives 0.01 accuracy
