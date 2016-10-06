#find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum

num=raw_input("Enter a number: ")
fnum=float(num)

#sum of first num numbers squared
s1=(fnum*(fnum+1)/2)**2
print s1

#sum of the squares of the first num numbers
i=0
s2=0
k=0
while i<fnum:
    k=k+2*i+1
    s2=s2+k
    i=i+1
print s2

print "The difference between the sum of the squares and the square of the sums of the first", fnum, "numbers is", s1-s2
    