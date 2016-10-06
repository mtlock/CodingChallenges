#starting at the top of the triangle and moving to adjacent
#numbers of the row below
#find the maximum total from top to bottom in Euler67.txt

tri=open("Euler67.txt")

D=dict()
i=0
for line in tri:
    line=line.rstrip()
    numbers=line.split()
    numbers=map(float, numbers)
    D[i]=numbers
    i=i+1


i=len(D)-1
while i>0:
    j=0
    while j<=len(D[i-1])-1:
        A=D[i-1][j]+D[i][j]
        B=D[i-1][j]+D[i][j+1]
        D[i-1][j]=max(A,B)
        j=j+1
    i=i-1
print D[0]