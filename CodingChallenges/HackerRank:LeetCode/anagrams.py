#Given an array of strings, return all groups of strings that are anagrams
#All inputs will be in lower case
#I assume no repeated words

strs = [x for x in raw_input().strip().split()]

 

#make a list of dictioaries for each entry, see if they're equal
    
    

def anagrams(strs):
    F = []
    G = {}
    for i in xrange(len(strs)):
        D = {}
        for j in xrange(len(strs[i])):
            D[strs[i][j]] = D.get(strs[i][j],0) + 1
        a = 0
        if D in F:
            a = F.index(D)
            G[a].append(strs[i])
        else:
            G[len(F)] = [strs[i]]
            F.append(D)
    return G

print anagrams(strs)
