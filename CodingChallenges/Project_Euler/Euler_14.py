# define iterative sequence
# n --> n/2 if n even
# n --> 3n+1 in n odd

#Conjecture that start with any number, the chain always ends in 1
#What is the starting number under 1 million which produces the longest chain?

# keys are number, values of length of chains
D=dict()
D[1]=1
D[2]=2
D[3]=8

maxlength=8
maxi=3
i=4
while i<=1000000:
    temp=i
    D[i]=1
    while temp>=i:
        if temp%2==0:
            temp=temp/2
            D[i]=D[i]+1
        else:
            temp=3*temp+1
            D[i]=D[i]+1
    D[i]=D[i]+D[temp]-1
    #print "The length is", D[i], "for the number", i
    if D[i]>maxlength:
        maxlength=D[i]
        maxi=i
    i=i+1
print "max length is", maxlength, "for the number", maxi
    
  

