#Larry has a permutation of N numbers, A, whose unique elements range from 1 to N (i.e. {a_1, a_2,...., a_N}).
#He wants A to be sorted, so he delegates the task of doing so to his robot.
#The robot can perform the following operation as many times as it wants:

#Choose any 3 consecutive indices and rotate their elements in such a way that ABC rotates to BCA, which rotates to CAB, which rotates back to ABC.

#On a new line for each test case, print "YES" if the robot can fully sort A, otherwise print "NO"

#Input format:
#The first line contains an integer, T, the number of test cases.
#The 2T subsequent lines each describe a test case over 2 lines:
    #1. An integer, N, denoting the size of A
    #2. N space-separated integers describing A, where the i-th value is element a_i
    
#Constraints:
#1<=T<=10
#3<=N<=1000
#1<=a_i<=N where every element a_i is unique (So it'll always be numbers 1-N)

T = int(raw_input().strip())

for j in xrange(T):
    N = int(raw_input().strip())
    A = [int(i) for i in raw_input().strip().split(' ')]
    
    i = 1
    while len(A)>3:
        ind = A.index(i)
        del A[ind]
        if ind % 2 != 0:
            t0 = A[0]
            t1 = A[1]
            A[0] = t1
            A[1] = t0   
        i=i+1
    if A[0]<A[2]<A[1] or A[2]<A[1]<A[0] or A[1]<A[0]<A[2]:
        print 'NO'
    else:
        print 'YES'
            

    
    
    
    
    
    
    
   