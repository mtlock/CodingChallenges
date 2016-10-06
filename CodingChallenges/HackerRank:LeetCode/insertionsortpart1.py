#def insertionSort(ar): 
#    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
#insertionSort(ar)

i=len(ar)-1
a=0
insert=ar[i]
while a==0:
    if insert>ar[i-1] or i==0:
        ar[i]=insert
        a=1
    else:
        ar[i]=ar[i-1]
    
    print ' '.join(str(x) for x in ar)
    i=i-1
    
#print ' '.join(['a','b'])
    