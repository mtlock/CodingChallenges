

a = int(raw_input('Enter a number '))

L = [int(i) for i in raw_input('Enter a list ').strip().split(' ')]

#The goal is to find what place a goes in the list, so we sort L first in case it isn't

L.sort()

#first = 0
#last = len(L)-1
#found = False
#midpoint = 1


def bsearch(a,L):
    first = 0
    last = len(L) - 1
    while first <= last:
        if first == last:
            if a == L[first]:
                return (1,first)
            else:
                return (-1,first)
        else:
            midpoint = (first + last)//2     
            if L[midpoint] == a:
                return (1,midpoint)
            elif L[midpoint] > a:
                last = midpoint
            else:
                first = midpoint   
                     
if bsearch(a,L)[0]<0:
    print a,'is not in the list'
else:
    print bsearch(a,L)[1]+1

#while first<=last and not found:
#    midpoint = (first + last)//2
#    if L[midpoint] == a:
#        found = True
#    elif L[midpoint] > a:
#        last = midpoint
#    else:
#        first = midpoint
        
#if found:
#    print a,'is in position',midpoint+1,'of the list'
#elif a < L[0]:
#    print a,'is not in the list, but would be inserted into the first position'
#elif a > L[len(L)-1]:
#    print a,'is not in the list, but would be inserted into the last position'
#else:
#    print a,'is not in the list, but would be inserted between the',first+2,'and',last+1,'positions'
