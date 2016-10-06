#Watson gives Sherlock an array  of length N.
#Then he asks him to determine if there exists an element in the array such that
#the sum of the elements on its left is equal to the sum of the elements on its right.
#If there are no elements to the left/right, then the sum is considered to be zero. 

#Input format:
#The first line contains T, the number of test cases. 
#For each test case, the first line contains N, the number of elements in the array A.
#The second line for each test case contains N space-separated integers, denoting the array A.

#Output:
#For each test case print YES if there exists an element in the array, such that the sum of the elements on its left is equal to the sum of the elements on its right; otherwise print NO.

T = int(raw_input().strip())

for j in xrange(T):
    N = int(raw_input().strip())
    A = [int(i) for i in raw_input().strip().split(' ')]
    
    indicator = 0
    
    if N == 1:
        indicator = 1
    else:
    
        lsum = 0
        rsum = sum(A[1:])
        
        i = 0    
        while i < N-1:
            if lsum == rsum:
                indicator = 1
                break
            else:
                lsum = lsum + A[i]
                rsum = rsum - A[i+1]
                i = i + 1
    
    if indicator == 1:
        print "YES"
    else:
        print "NO"
            