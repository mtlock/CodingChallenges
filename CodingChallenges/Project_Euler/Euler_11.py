#import the 20x20 grid of numbers, find the greatest product of four adjacent numbers in the same direction
#up, down, left, right, diagonal
grid=open("Euler_11.txt", 'r')
D=dict()
i=0
for line in grid:
    line=line.rstrip()
    numbers=line.split()
    numbers=map(int, numbers)
    D[i]=numbers
    i=i+1

dprod1=1
dprod2=1
hprod=1
vprod=1
tdprod1=1
tdprod2=1
thprod=1
tvprod=1
#down to the right diagonal
i=0
while i<=16:
    L0=D[i]
    L1=D[i+1]
    L2=D[i+2]
    L3=D[i+3]
    k=0
    while k<=16:
        tdprod1=L0[k]*L1[k+1]*L2[k+2]*L3[k+3]
        if tdprod1>dprod1:
            dprod1=tdprod1
        k=k+1
    i=i+1   
#print dprod1
#down to the left diagonal
i=0
while i<=16:
    L0=D[i]
    L1=D[i+1]
    L2=D[i+2]
    L3=D[i+3]
    k=3
    while k<=19:
        tdprod2=L0[k]*L1[k-1]*L2[k-2]*L3[k-3]
        if tdprod2>dprod2:
            dprod2=tdprod2
        k=k+1
    i=i+1   
#print dprod2
#horizontal
i=0
while i<=19:
    L=D[i]
    k=0
    while k<=16:
        thprod=L[k]*L0[k+1]*L0[k+2]*L0[k+3]
        if thprod>hprod:
            hprod=thprod
        k=k+1
    i=i+1   
#print hprod
#vertical 
i=0
while i<=16:
    L0=D[i]
    L1=D[i+1]
    L2=D[i+2]
    L3=D[i+3]
    k=0
    while k<=19:
        tvprod=L0[k]*L1[k]*L2[k]*L3[k]
        if tvprod>vprod:
            vprod=tvprod
        k=k+1
    i=i+1   
#print vprod
print max([dprod1,dprod2,hprod,vprod])













