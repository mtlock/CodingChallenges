#What is the 10001 prime number


primes=[2,3,5,7]

i=9
while len(primes)<10001:
    a=0
    k=0
    while k<len(primes)-1:
        if primes[k]>i**(.5):
            break
        elif i%primes[k]==0:
            a=1
            break
        else:
            k=k+1
    if a==1:
        i=i+2
        continue
    else:
        primes.append(i)
        i=i+2
print primes[len(primes)-1]   
        
    


