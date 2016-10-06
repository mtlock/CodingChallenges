#rotate an MxN matrix, where at least the smaller of M and N is even, by R

import sys

M,N,R = raw_input().strip().split(' ')
M,N,R = [int(M),int(N),int(R)]


L=[]
for a0 in xrange(M):
    n = raw_input().strip().split(' ')
    L.append(n)
    

loops=min(M,N)/2 
    
D={}
j=0
while j<loops:
    temp1=[]
    temp2=[]
    temp3=[]
    temp4=[]
    i=0
    while i<N-1-2*j:
        temp1.append(L[j][i+j])
        temp3.append(L[M-1-j][N-1-j-i])
        i=i+1
    i=0
    while i<M-1-2*j:
        temp2.append(L[i+j][N-1-j])
        temp4.append(L[M-1-i-j][j])
        i=i+1 
    D[j]=temp1+temp2+temp3+temp4
    j=j+1

E={}   
j=0
while j<loops:
    k=0
    list=[]
    while k<len(D[j]):
        list.append(D[j][(k+R)%len(D[j])])
        k=k+1
    E[j]=list
    j=j+1


i=0
temp=[]
while i<=M-1:
    if N-2*i>0 and i<=(M-1)/2:
        temp=E[i][:N-2*i]
    elif N-2*(M-1-i)>0:
        temp=E[M-i-1][N-4*(M-i-1)+M-2:2*N-6*(M-i-1)+M-2]
        temp.reverse()
    else:
        temp=[]
    a=[]
    b=[]
    j=0
    while len(temp)+len(a)+len(b)<N:
        a.append(E[j][len(E[j])-i+j])
        b.append(E[j][max(N-2*j,0)+i-j-1])
        j=j+1
    b.reverse()
    print ' '.join(a+temp+b)
    #print ' '.join(temp)
    i=i+1
    


