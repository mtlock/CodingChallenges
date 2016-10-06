# find the sum of all of the primes below 2 million

sum=2
primes=[2]
i=3
while i<2000000:
    for prime in primes:
        if prime>(i**(.5)):
            primes.append(i)
            sum=sum+i
            break
        elif i%prime==0:
            break
    i=i+2
print sum
    
    