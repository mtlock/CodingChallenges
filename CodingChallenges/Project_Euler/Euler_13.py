#What are the first 10 digits of the sum of the numbers

file=open("Euler_13.txt")
D=dict()
E=dict()
i=0
for line in file:
    line=line.rstrip()
    for j in range(0,14):
        D[j]=D.get(j,0)+int(line[j])
    i=i+1
    
sum=0
for j in range(0,14):
    D[j]=D[j]*((10)**(13-j))
    sum=sum+D[j]

print sum

#5537376229920, 10
#5537376230390360, 13


