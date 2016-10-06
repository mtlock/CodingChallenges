#Given an array S of n integers, are there elements a,b,c,d in S
#such that a+b+c+d=target?
#Find all unique quadruplets in the array which gives the sum of target
#Elements in a quadruplet must be in non-descending order
#No duplicate quadruplets


def fourSum(L, target):
    L.sort()
    n=len(L)
    res=[]
    for i in range(n-3):
        if i>0 and L[i-1]==L[i]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and L[j-1]==L[j]:
                continue
            k=j+1
            l=n-1
            while k<l:
                s=L[i]+L[j]+L[k]+L[l]
                if s==target:
                    res.append([L[i],L[j],L[k],L[l]])
                    k+=1
                    l-=1
                    while k<l and L[k]==L[k-1]:
                        k+=1
                    while k<l and L[l]==L[l+1]:
                        l-=1
                elif s<target:
                    k+=1
                else:#s>target:
                    l-=1
    return res


target = input()
L = [int(i) for i in raw_input().strip().split()]
answer=fourSum(L,target)
for item in answer:
    print item
    