m = input()
ar = [int(i) for i in raw_input().strip().split()]


j=1
while j<len(ar):

    i=len(ar[:j])
    a=0
    insert=ar[i]
    while a==0:
        if insert>ar[i-1] or i==0:
            ar[i]=insert
            a=1
        else:
            ar[i]=ar[i-1]
        i=i-1
    print ' '.join(str(x) for x in ar)
    
    j=j+1
    
#This is O(n^2)