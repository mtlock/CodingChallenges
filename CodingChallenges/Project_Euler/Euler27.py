#first make a huge list of primes
#dictionary has -1 if not prime, 1 if prime
D={1:-1,2:1,3:1}
L=[2,3]
i=4
while len(L)<5000:
    a=0
    j=0
    while L[j]<=i**.5:
        if i%L[j]==0:
            a=1
            D[i]=-1
            break
        j=j+1
    if a==0:
        D[i]=1
        L.append(i)
    i=i+1

#997 is largest prime less than 1000



def f(a,b,n):
    return n**2+a*n+b

 
def tcount(a,b):
    i=1
    tcount=1
    while i<500:
        if f(a,b,i)<=0 or D[f(a,b,i)]!=1:
            break
        else:
            tcount=tcount+1  
        i=i+1
    return tcount

#print tcount(1,41)    

count=1
maxA=1
maxB=1
j=1
while j<170:
    a=-999
    while a<1000:
        if tcount(a,L[j])>count:
            #print tcount(a,L[j])
            count=tcount(a,L[j])
            maxA=a
            maxB=L[j]
            #count=tcount
        a=a+1
    j=j+1
print count
print maxA
print maxB

