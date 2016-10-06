# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

M,N,R = raw_input().strip().split(' ')
M,N,R = [int(M),int(N),int(R)]

L=[]
for a0 in xrange(M):
    n = raw_input().strip().split(' ')
    L.append(n)



loops=min(M,N)/2     



#separate each loop into 4 parts
j=0
H1={}
H2={}
H3={}
H4={}
while j<loops:
    H1[j]=[]
    H2[j]=[]
    H3[j]=[]
    H4[j]=[]
    #temp2=[]
    #temp3=[]
    #temp4=[]
    i=0
    while i<N-1-2*j:
        H1[j].append(L[j][i+j])
        H3[j].append(L[M-1-j][N-1-j-i])
        i=i+1
    i=0
    while i<M-1-2*j:
        H2[j].append(L[i+j][N-1-j])
        H4[j].append(L[M-1-i-j][j])
        i=i+1 
    #H1[j]=temp1
    #H2[j]=temp2
    #H3[j]=temp3
    #H4[j]=temp4
    j=j+1
    
    
    
#j=0
#H1={}
#H2={}
#H3={}
#H4={}
#while j<loops:
#    temp1=[]
#    temp2=[]
#    temp3=[]
#    temp4=[]
#    i=0
#    while i<N-1-2*j:
#        temp1.append(L[j][i+j])
#        temp3.append(L[M-1-j][N-1-j-i])
#        i=i+1
#    i=0
#    while i<M-1-2*j:
#        temp2.append(L[i+j][N-1-j])
#        temp4.append(L[M-1-i-j][j])
#        i=i+1 
#    H1[j]=temp1
#    H2[j]=temp2
#    H3[j]=temp3
#    H4[j]=temp4
#    j=j+1

i=0
while i<R:
    j=0
    while j<loops:
        t1=H1[j][0]
        t3=H3[j][0]
        k=0
        while k<len(H1[j])-1:
            H1[j][k]=H1[j][k+1]
            H3[j][k]=H3[j][k+1]
            k=k+1
        H1[j][len(H1[j])-1]=H2[j][0]
        H3[j][len(H3[j])-1]=H4[j][0]
        k=0
        while k<len(H2[j])-1:
            H2[j][k]=H2[j][k+1]
            H4[j][k]=H4[j][k+1]
            k=k+1
        H2[j][len(H2[j])-1]=t3
        H4[j][len(H4[j])-1]=t1
        j=j+1
    i=i+1
    
    
    
 
j=0
while j<loops:
    H3[j].reverse()
    H4[j].reverse()
    j=j+1


D={}
i=0
while i<=(M-1):
    try:
        tempstring=' '.join(H1[i])
        D[i]=D.get(i,'')+tempstring+' '
    except:
        try:
            tempstring=' '.join(H3[M-i-1])
            D[i]=D.get(i,'')+tempstring+' '
        except:
            pass
    j=0
    a=''
    b=''
    while j<i:
        try:
            a=a+H4[j][i-1-j]+" "
            b=H2[j][i-j]+' '+b
        except:
            break
        j=j+1
    try:
        b=H2[i][0]+' '+b
    except:
        pass
    D[i]=a+D.get(i,'')+b
    print D[i]
    i=i+1
    

    


