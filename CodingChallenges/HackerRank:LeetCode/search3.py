#Maximize sum

#You are given an array of size N and another integer M. 
#Your target is to find the maximum value of sum of subarray modulo M.

#Subarray is a continuous subset of array elements.

#Note that we need to find the maximum value of (Sum of Subarray)%M , where there are Nx(N+1)/2 possible subarrays.

#For a given array A of size N , subarray is a contiguous segment from i to j where 0<=i,<=j<=N

#Input Format 
#First line contains T , number of test cases to follow. Each test case consists of exactly 2 lines. 
#First line of each test case contain 2 space separated integers N and M, size of the array and modulo value M. 
#Second line contains N space separated integers representing the elements of the array.

#Output Format 
#For every test case output the maximum value asked above in a newline.

#Constraints 
#1<=elements of the array <=10^{18}


import math

def closest(sum_i,L):
        temp = []
        for num in L:
            if num > sum_i:
                temp.append(num)
        if len(temp)>=1:
            return (sum_i-min(temp))%M
        else:
            return sum_i
        



T = int(raw_input().strip())



for j in xrange(T):
    n , m = raw_input().strip().split(' ')
    N = int(n)
    M = int(m)
    A = [int(i)%M for i in raw_input().strip().split(' ')]
    
    max = 0
    F = [0]
    i=1
    while i <= N:
        F.append((F[i-1]+A[i-1])%M)
        if closest(F[i],F[:i]) > max:
            max = closest(F[i],F[:i])
    
    
    
        i=i+1
    
    #max = 0
    #i = 1
    #while i<=N:
    #    if closest(F[i],F[:i]) > max:
    #        max = closest(F[i],F[:i])
    #    i=i+1
    print max
    
    
      
    #max = 0  
    #i=1
    #while i <= N:
    #    temp = closest(F[i],F[:i])
    #    if closest(F[i],F[:i]) > max:
    #        max = temp
    #    
    #    if max == M - 1:
    #        break
     #   else:
     #       i = i+1
            
    
   
        