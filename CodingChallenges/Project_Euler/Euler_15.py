#Starting at the top left corner of a 20x20 grid, and only being able to move to the right and down,
#how many roots are there to the bottom right corner?

#40 choose 20, but can you code to make a list of all possible paths?


#D=dict()
hcount=dict()
vcount=dict()
hcount[0]=0
vcount[0]=0
L=list()
L.append(0)
Ltemp=list()
#finallist=list()
i=1
count=1
while True:
    #a=0
    if len(L)==0:
        break
    else:
        for k in L:
            if hcount[k]==10 or vcount[k]==10:
                #finallist.append(k)
                L.remove(k)
                #count=count+1
                #a=a+1
            else:
                #D[k+i]=D.get(k,"")+"v"
                #D[k]=D.get(k,"")+"h"
                hcount[k+i]=hcount.get(k,0)
                vcount[k+i]=vcount.get(k,0)+1
                hcount[k]=hcount.get(k,0)+1
                Ltemp.append(k+i)
                count=count+1
        L=L+Ltemp
        del Ltemp[:]
    #if len(L)==0:
     #   break
    i=2*i
#print finallist
print count
print len(L)