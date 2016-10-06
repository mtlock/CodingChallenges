#A palindromic number reads the same both ways. 
#Find the largest palindrome made from the product of two 3-digit numbers.

lst=list()
x=100
while x<1000:
    y=999
    while y>=x:
        p=str(x*y)
        if len(p)%2==0:
            i=1
            z=0
            while i<=(len(p))/2:
                if p[i-1]!=p[len(p)-i]:
                    z=1
                    break
                i=i+1
            if z==0:
                lst.append((int(p),x,y))
        else:
            i=1
            z=0
            while i<=(len(p)-1)/2:
                if p[i-1]!=p[len(p)-i]:
                    z=1
                    break
                i=i+1
            if z==0:
                lst.append((int(p),x,y))        
        y=y-1
    x=x+1
lst.sort()
biggest=lst[len(lst)-1]
print "The largest palindrom that is a multple of two three digit number is", biggest[0],"which is a multiple of", biggest[1],"and",biggest[2]