#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143?

#Change it to enter a number and find largest prime factor

num=raw_input("Enter an odd integer: ")
fnum=float(num)
i=3
lst=list()
while i<=fnum:
    k=3
    a=0
    if fnum%i==0:
        while k<i:
            if i%k==0:
                a=1
            k=k+2
        if a==0:
            lst.append(i)
            fnum=fnum/i
    i=i+1
print "The prime factors are", lst
print "The largest prime factor is", lst[len(lst)-1]