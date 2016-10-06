# Find the 13 adjacent digits in the 1000-digit number in Euler_8.txt that have the greatest product.
# What is the value of this product?

fhandle=open("Euler_8.txt")
num=fhandle.read()
string=""
for line in num:
    line=line.rstrip()
    string=string+line
i=0
a=0
maxstring=string[0:13]
maxprod=1
tempprod=1
while i<=12:
    maxprod=maxprod*int(string[i])
    i=i+1
while i<=len(string)-1:
    if int(string[i])<=int(string[i-13]):
        a=1
        i=i+1
        continue
    elif int(string[i-13])==0 or a==1:
        k=0
        tempprod=1
        while k<=12:
            tempprod=tempprod*int(string[i-k])
            k=k+1
        a=0
    else:
        tempprod=tempprod*(int(string[i]))/(int(string[i-13]))
        a=0
        
    if tempprod>maxprod:
        maxprod=tempprod
        maxstring=string[i-12:i+1]
    i=i+1

print maxprod
