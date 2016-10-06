
import sys

a=raw_input("enter a string: ").strip()
b=raw_input("enter a string: ").strip()


L=[]
for chara in a:
    if chara in L:
        continue
    else:
        try:
            b.index(chara)
            L.append(chara)
        except:
            b.replace(chara,'')

La=[a]
Lb=[b]        
X=[]
Y=[]
i=0
while len(La)>0 and len(Lb)>0:    
    k=0
    while k<len(La):
        l=k+1
        while l<len(La):
            if len(La[l])>len(La[k]) and len(Lb[l])>len(L[k]):
                l=l+1
                break
            l=l+1
        if l==len(La):
            X.append(La[k])
            Y.append(Lb[k])    
        k=k+1
    print X
    print Y
   
    La=[]
    Lb=[]
    j=0
    while j<len(X):
        for char in L:
            try:
                if X[j].index(char)<len(X[j])-1 and Y[j].index(char)<len(Y[j])-1:
                    La.append(X[j][X[j].index(char)+1:])
                    Lb.append(Y[j][Y[j].index(char)+1:])     
            except:
                pass
        j=j+1
    i=i+1
    
print i-1    
                  
            
            
        