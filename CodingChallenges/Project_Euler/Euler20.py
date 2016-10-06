#Find the sum of the digits in the number 100!

#first, find the a list of primes from 1-100
import math

i=2.0
primes=dict()
while i<100:
    k=2
    a=0
    while k<=(i)**(.5):
        if i%k==0:
            a=1
            break
        k=k+1
    if a==0:
        primes[i]=1
    i=i+1
lst=primes.keys()

i=4
while i<=100:
    temp=i
    for p in lst:
        while p<=i/2 and temp>1:
            if temp%p==0:
                temp=temp/p
                primes[p]=primes[p]+1
            else:
                break
    i=i+1
    
factorial=1
for p in lst: 
    factorial=factorial*(p**(primes[p]))
#factorial=factorial/((5**primes[5])*(2**primes[5]))
#print int(factorial)


#the above appears to give the wrong number



i=1
num=1
while i<=100:
    num=num*i
    i=i+1

snum=str(num)
i=0
sum=0
while i<len(snum):
    sum=sum+int(snum[i])
    i=i+1
print sum





#print primes    
#factorial=1
#for p in lst:
#    if p==2 or p==5:
#        continue
#    else:
#        factorial=factorial*(p**(primes[p]))
#factorial=factorial*(2**(primes[2]-primes[5])

#print factorial
#print len(factorial)
#print str
#fstring=str(factorial)
#sum=0
#print len(string)
#for s in fstring:
#    print s
    #int_s=int(s)    
    #sum=sum+int_s
#print sum      
