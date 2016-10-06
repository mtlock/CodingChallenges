# Given an array S of n integers, find three integers in S such that the sum is
# closest to a given target number
#Return the sum of the three integers
#You may assume that each input would have exactly one solution


def threeSumCloset(L,target):
    L.sort()
    res=L[0]+L[1]+L[2]
    for i in range(len(L)-2):
        l=i+1
        r=len(L)-1
        while l<r:
            s=L[i]+L[l]+L[r]
            if abs(s-target)<abs(res-target):
                res=s
            if s==target:
                return s
            elif s<target:
                l+=1
            else:#s>target
                r-=1
    return res



target = input()
L = [int(i) for i in raw_input().strip().split()]
print threeSumCloset(L,target)
