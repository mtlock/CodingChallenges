def partition(l):  
    p=l[0]
    left=[]
    #equal=[p]
    right=[]
    for char in l:
        if char<p:
            left.append(char)
        elif char>=p:
            right.append(char)
    string=' '.join(str(x) for x in left)+' '+' '.join(str(x) for x in right)
    return string
m = input()
ar = [int(i) for i in raw_input().strip().split()]
print partition(ar)
