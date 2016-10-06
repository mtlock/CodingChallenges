import sys

a=raw_input("enter a string: ").strip()
b=raw_input("enter a string: ").strip()


def reduce(x,y):
    L=[]
    min=len(y)
    for char in x:
        if char in L:
            continue
        else:
            try:
                if y.index(char)<min:
                    min=y.index(char)
                    L.append(char)
            except:
                x.replace(char,'')
               
                #ind=y.index(char)
                #a=0
                #for char2 in L:
                #    if y.index(char2)<ind:
                #        a=1
                #        break
                #if a==0:
                #    L.append(char)
            #except:
                #x.replace(char,'')
    return (x,y,L)






#def reduce(x,y):
#    Dx={}
#    Dy={}
#    L=[]
#    for char in x:
#        Dx[char]=Dx.get(char,0)+1
#        if Dx[char]==1:
#            L.append(char)
#        Dy[char]=0
#    for char in y:
#        Dy[char]=Dy.get(char,0)+1
#        Dx[char]=Dx.get(char,0)
#    for char in Dx:
#        if Dy[char]==0:
#            L.remove(char)
#    for char1 in L:
#        for char2 in L[L.index(char1)+1:]:
#            if x.index(char1)<x.index(char2) and y.index(char1)<y.index(char2):
#                    
#                L.remove(char2)
#    return (x,y,L)       



            
            


count=0
a,b,L=reduce(a,b)
lena=len(a)
lenb=len(b)
ind=0
if len(L)==0:
    print 0
else:
    D={}
    D[0]=[a,b]
    i=0
    max=len(L)
    while max>0:
        #print len(D)
        m1=0
        m2=0
        temp=D
        max=0
        D={}
        j=0
        for element in temp:
            if len(temp[element][0])<m1 and len(temp[element][1])<m2:
                count=count+1
                continue
            elif len(temp[element][0])>m1 and len(temp[element][1])>m2:
                m1=len(temp[element][0])
                m2=len(temp[element][1])
                compareto=j
            x,y,L=reduce(temp[element][0],temp[element][1])
            
            
            if len(L)>max:
                max=len(L)
   
            for char in L:
                #if (x.index(char)+1,y.index(char)+1)>min:
                #    continue
                #elif (x.index(char)+1,y.index(char)+1)<min:
                #    min=(x.index(char)+1,y.index(char)+1)
                tlist=[x[x.index(char)+1:],y[y.index(char)+1:]]
                D[j]=tlist
                j=j+1   
           
        i=i+1
    #print count, i-1
    print i-1
     