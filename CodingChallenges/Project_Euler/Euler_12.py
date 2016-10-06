#what is the first triangular number with over 500 divisors

#first, make a list of primes

primes=[2]
i=3
while i<10000:
    for prime in primes:
        if prime>(i**(.5)):
            primes.append(i)
            break
        elif i%prime==0:
            break
    i=i+2

tri=[1]
i=1
while i<100000:
    newtri=tri[i-1]+(i+1)
    tri.append(newtri)
    i=i+1

i=0
while i<100000:
    temp=tri[i]
    prod=1
    for p in primes:
        if p>temp:
            break
        a=0
        j=0
        while a==0:
            if temp%p==0:
                temp=temp/p
                j=j+1
                continue
            else:
                a=1
        prod=prod*(j+1)
    if prod>500:
        print tri[i]
        break
    i=i+1
        

        
    
    
