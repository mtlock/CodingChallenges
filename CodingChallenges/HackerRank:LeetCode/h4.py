# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

a=raw_input().strip()
b=raw_input().strip()



def reduce(x,y):
    Dx={}
    Dy={}
    L=[]
    for char in x:
        Dx[char]=Dx.get(char,0)+1
        if Dx[char]==1:
            L.append(char)
        Dy[char]=0
    for char in y:
        Dy[char]=Dy.get(char,0)+1
        Dx[char]=Dx.get(char,0)
    for char in Dx:
        if Dx[char]==0:
            y=y.replace(char,'')
        elif Dy[char]==0:
            x=x.replace(char,'')
            L.remove(char)
    return (x,y,L)       


#def secondreduce(x,y,L):
#    T=[]
#    H={}
#    l=0
#    for char in L:
#        try:
#            if x.index(char)<len(x)-1 and y.index(char)<len(y)-1:
#                H[l]=[x[x.index(char)+1:],y[y.index(char)+1:]]
                #x.index(char)
                #y.index(char)
#                T.append(char)
#                l=l+1
#        except:
            #x=x.replace(char,'')
            #y=y.replace(char,'')
#            pass
#    return (x,y,T,l,H)
            
            



a,b,L=reduce(a,b)
D={}
D[0]=[a,b]
i=0
max=len(L)
while max>0:
#while len(D)>1:
    max=0
    temp=D
    
    D={}
    j=0
    for element in temp:
        #x,y,T,l,H=secondreduce(temp[element][0],temp[element][1],L)
        x,y,L=reduce(temp[element][0],temp[element][1])
        for char1 in L:
            for char2 in L[L.index(char1)+1:]:
                if x.index(char1)<x.index(char2) and y.index(char1)<y.index(char2):
                    #print char1,char2
                    #print x.index(char1),x.index(char2)
                    #print y.index(char1),y.index(char2)
                    L.remove(char2)
        if len(L)>max:
            max=len(L)
        #k=1
        #while k<=l:
            #D[j+k]=H[k-1]
        for char in L:
            if x.index(char)<len(x)-1 and y.index(char)<len(y)-1:
                tlist=[x[x.index(char)+1:],y[y.index(char)+1:]]
                D[j]=tlist
                j=j+1   
        #j=j+1
        
        
        #x,y,L=reduce(temp[element][0],temp[element][1]) 
        #print L
        #for char1 in L:
        #    for char2 in L[L.index(char1)+1:]:
        #        if x.index(char1)<x.index(char2) and y.index(char1)<y.index(char2):
                    #print char1,char2
                    #print x.index(char1),x.index(char2)
                    #print y.index(char1),y.index(char2)
        #            L.remove(char2)
        
        #if len(L)>max:
        #    max=len(L)
        #if j==30000:
        #    break
        #for char in L:
        #    if x.index(char)<len(x)-1 and y.index(char)<len(y)-1:
        #        tlist=[x[x.index(char)+1:],y[y.index(char)+1:]]
        #        D[j]=tlist
        #        j=j+1   
    i=i+1
print i-1
            
