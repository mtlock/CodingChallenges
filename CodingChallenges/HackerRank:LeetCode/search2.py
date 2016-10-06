#Sunny and Johnny together have M dollars they want to spend on ice cream.
#The parlor offers N flavors, and they want to choose two flavors so that they end up spending the whole amount.

#You are given the cost of these flavors. The cost of the ith flavor is denoted by c_i.
#You have to display the indices of the two flavors whose sum is M.

#Input format
#The first line of the input contains T;T  test cases follow. 
#Each test case follows the format detailed below: The first line contains M.
#The second line contains N. The third line contains N space-separated integers denoting the price of each flavor. Here, the ith integer denotes c_i.

#Output Format
#Output two integers, each of which is a valid index of a flavor. 
#The lower index must be printed first. Indices are indexed from 1 to N.

#The prices of any two items may be the same and each test case has a unique solution.



T = int(raw_input().strip())

for j in xrange(T):
    M = int(raw_input().strip())
    N = int(raw_input().strip())
    C = [int(i) for i in raw_input().strip().split(' ')]
    
    for i in xrange(N):
        dif = M - C[i]
        if dif in C[i+1:]:
            D = C[i+1:]
            ind1 = i
            ind2 = D.index(dif)+i+1
            break
    print ind1+1,ind2+1
    
    