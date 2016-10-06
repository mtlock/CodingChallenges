#Given 2 binary strings, return their sum (also a binary string)


def addbinary(a,b):
    res=[]
    #make s1 the longer of the two
    if len(a)<len(b):
        b,a=a,b
    n=len(a)
    m=len(b)
    c=0 #carry
    r=0 #result
    for i in range(n):
        j=n-1-i
        if i<m:
            k=m-1-i
            r=(int(a[j])+int(b[k])+c)%2
            c=(int(a[j])+int(b[k])+c)/2
        else:
            r=(int(a[j])+c)%2
            c=(int(a[j])+c)/2
        res.insert(0,str(r))
    if c==1:
        res.insert(0,str(c))
    return ''.join(res)




s1=raw_input("enter the first string: ")
s2=raw_input("enter the second string: ")
print addbinary(s1,s2)
