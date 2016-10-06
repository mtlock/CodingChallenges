def partition(ar):  
    p=ar[0]
    left=[]
    #equal=[]
    right=[]
    for char in ar:
        if char<p:
            left.append(char)
        #elif char==p:
            #equal.append(char)   
        elif char>p:
            right.append(char)
    #string=' '.join(str(x) for x in left)+' '+' '.join(str(x) for x in right)
    #return string
    return left,p,right
    #return left+equal+right
    
   
def quicksort(ar):
    L=[]
    while len(ar)>0:
        if len(partition(ar)[0])==0:       
            L.append(partition(ar)[1])
            ar=partition(ar)[2]
        else:
            ar=partition(ar)[0]+[partition(ar)[1]]+partition(ar)[2]
    #string=' '.join(str(x) for x in L)
    return L
    
    
    
    
m = input()
ar = [int(i) for i in raw_input().strip().split()]
print quicksort(ar)

#print partition(ar)