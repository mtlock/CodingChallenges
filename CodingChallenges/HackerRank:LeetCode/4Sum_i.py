#Given an array S of n integers, are there elements a,b,c,d in S
#such that a+b+c+d=target?
#Find all unique quadruplets in the array which gives the sum of target
#Elements in a quadruplet must be in non-descending order
#No duplicate quadruplets


#return a list of lists of length 4


def threeSum(num,first,t):          
    res1=[]
    i=0
    while i<=len(num)-3:
        if num[i]>=t:
            break
        else:
            j=i+1
            while j<=len(num)-2:
                s=t-(num[i]+num[j])
                if [first,num[i],num[j],s] in res1:
                    j=j+1
                    continue
                elif s>=num[j+1] and s in num:
                    res1.append([first,num[i],num[j],s])
                j=j+1
        i=i+1   
    return res1 

def fourSum(L,target):
    L.sort()
    n=len(L)
    res2=[]
    for i in range(n-3):
        t=target-L[i]
        temp=threeSum(L[i+1:],L[i],t)
        for item in temp:
            if item in res2:
                continue
            else:
                res2.append(item)
            
    return res2
        
        


target = input()
L = [int(i) for i in raw_input().strip().split()]
answer=fourSum(L,target)
for item in answer:
    print item
    
