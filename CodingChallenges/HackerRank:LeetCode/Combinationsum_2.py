#Given a set of candidate number (C) and a target number (T)
#find all unique combinations in C where the candidate numbers
#sum to T
#Each number in C can be used at most once
#All numbers will be positive integers
#Elements in a combination must be listed in ascending order


print "Enter C"
C = [int(i) for i in raw_input().strip().split()]
T = int(raw_input("Enter T "))

C.sort()


#sum=0
#g_ind=0
#for i in range(len(C)-1,-1,-1):
#    sum = sum + C[i]
#    if C[i] > T:
#        gind = i
    
#C=C[:gind]
#if sum < T:
#    print "No combination"


def combination(C,T):
    res = []
    cand = []
    #candidates.sort()
    combination_sum(C, cand, T, res)
    return res
 
def combination_sum(C,cand, T,res):  
    if T == 0:     
        res.append(cand[:])      
    elif T < 0 or len(C)==0:
        return
    #elif T == 0:
    #    res.append(cand[:])
    else:
        temp = C[0]
        L = cand
        L.append(temp)
        C = C[1:]
        combination_sum(C,L, T-temp,res)
        combination_sum(C,cand, T,res)
        
    
 
    
#def combination_sum(C,cand, T,res): 
#    print T
    #temp = C[0]
#    if T == 0:
#        print T
#        print cand
#        res.append(cand[:])
        #print cand[:]
        #return
#    elif len (C) == 0:
#        return
#    elif T<0:#T - C[0]<0:
#        return
    
    #elif T < 0 or len(C) == 0:
        #print "a", res
    #    return
    #elif T == 0:
        #cand.append(C[0])
    #    res.append(cand)
#    else:
#        temp = C[0]
#        C = C[1:]
#        combination_sum(C,cand, T,res)
        #cand1 = cand
        #cand1 = cand
#        cand.append(temp)
#        combination_sum(C,cand, T-temp,res) 
        #combination_sum(C,cand, T,res)
            
print combination(C,T)
for l in combination(C,T):
    print sum(l)
        

#print len(C[1:])

    #if T<0:
    #    return
    #elif T == 0:
    #    res.append(cand[:])
    #else:
    #    for i,c in enumerate(candidates):
    #        cand.append(c)
    #        combination_sum(candidates[i:],cand, T -c, res)
    #        cand.pop()         

    