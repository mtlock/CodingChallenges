# Given an array S of n integers, are there elements a,b,c in S
#such that a+b+c=0?
#Find all unique triplets in the array which gives the sum of zero
#Elements in a triplet a,b,c must be in non-descending order 
#The solution set must not contain duplicate triplets

#return a list of lists of length 3 [[val1,val2,val3]]
def threeSum(num):
    num.sort()
    #L=[]
    #for n in num:
    #    if n in L:
    #        continue
    #    else:
    #        L.append(n)              
    res=[]
    i=0
    while i<=len(num)-3:
        if num[i]>=0:
            break
        else:
            j=i+1
            while j<=len(num)-2:
                s=-(num[i]+num[j])
                if [num[i],num[j],s] in res:
                    j=j+1
                    continue
                elif s>=num[j] and s in num:
                    res.append([num[i],num[j],s])
                j=j+1
        i=i+1
    
    return res               
                
num= [int(i) for i in raw_input().strip().split()]    
print threeSum(num)

    