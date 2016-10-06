#There are n chapters in a workbook, numbered 1-n
#The i-th chapter has t_i problems numbered 1-t_i
#Each page can hold up to k problems
#There are no empty pages or unnecessary spaces, so only the last page
#of a chapter may contain fewer than k problems
#Each new chapter starts on a new page, so a page will never contain problems
#from more than one chapter
#The page number indexing starts at 1

#The problem is special if its index within a chapter is the same as the page number
#where it is located

#Given the details of the workbook, how many special problems are there?

#Input format:
#The first line contains two integers, n and k
#The second line contains integers t_1,t_2,...,t_n

#Constraints:
#1<=n,k,t_i<=100

#Output the number of special problems in the workbook


n,k = raw_input().strip().split(' ')
n,k = int(n),int(k)

T = [int(i) for i in raw_input().strip().split(' ')]
count = 0
page = 1
for i in xrange(n):
    problem = 1
    while problem <= T[i]:
        if problem <= page <= problem + k - 1:
            if problem + k - 1 <= T[i]:
                count = count + 1
            elif T[i] >= page:
                count = count + 1
        page = page + 1
        problem = problem + k    

print count  





#P = []
#pages = 0
#for i in xrange(n):
#    p = math.ceil(T[i]/k)
#    problem = 1
#    for j in xrange(p):
#        pages = pages + 1
#        P.append((problem,problem+k-1,pages))
#        problem = problem
    

