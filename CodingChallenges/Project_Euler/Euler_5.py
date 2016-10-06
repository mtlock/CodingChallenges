#2520 is the smallest number that can be divided by each of the numbers 
#from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all 
#of the numbers from 1 to 20?


#first, find the a list of primes from 1-20
i=2.0
primes=dict()
while i<20:
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

#next, find the max each prime occurs in the factorizations of the numbers from 1-20
i=2
while i<=20:
    k=0
    while k<=len(lst)-1:
        count=primes[lst[k]]
        if i<=lst[k]:
            break
        if i%lst[k]**primes[lst[k]]==0:
            while lst[k]**(count+1)<=i:
                if i%(lst[k]**(count+1))!=0:
                    break
                count=count+1
            if primes[lst[k]]<count:
                primes[lst[k]]=count
        k=k+1
    i=i+1
print primes
k=0
product=1
while k<=len(lst)-1:
    product=product*(lst[k]**primes[lst[k]])
    k=k+1
print "The least common multiple is", product
            
        
    

