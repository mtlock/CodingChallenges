#Given a set of candidate number (C) and a target number (T)
#find all unique combinations in C where the candidate numbers
#sum to T
#The same repeated number may be chosen as many times as you'd like
#All numbers will be positive integers
#Elements in a combination must be listed in non-descending order


print "Enter C"
C = [int(i) for i in raw_input().strip().split()]
T = int(raw_input("Enter T "))


def combinationSum(candidates,target):
    res = []
    cand = []
    candidates.sort()
    combination_sum(candidates, cand, target, res)
    return res
    
def combination_sum(candidates,cand,target,res):
    if target<0:
        return
    elif target == 0:
        res.append(cand[:])
    else:
        for i,c in enumerate(candidates):
            cand.append(c)
            combination_sum(candidates[i:],cand, target -c, res)
            cand.pop()    


    
print combinationSum(C,T)
        