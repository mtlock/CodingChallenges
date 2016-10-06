# list primes under 1000 (didn't use this)

lst=list()
lst.append(2)
for i in range (3,1000):
    for L in lst:
        if L>i**.5:
            lst.append(i)
            break
        elif i%L==0:
            break

# dictionary of sum of proper divisors

D=dict()
sum=1
for i in range (4,10000):
    for k in range (2,i):
        if i%k==0:
            d=k
            if i/k==k:
                sum=sum+d
            else:
                sum=sum+d+i/d
            break
    for k in range (d+1,int(i**.5)+1):
        if i%k==0:
            if i/k==k:
                sum=sum+k
            else:
                sum=sum+k+i/k
    D[i]=sum
    sum=1

    
compare=0
sum=0
for i in range (4,10000):
    compare=D[i]
    if compare<10000 and compare>=4 and compare!=i:
        if D[compare]==i:
            print compare
            sum=sum+compare
print sum
        
        
    
        
                
    
    
            