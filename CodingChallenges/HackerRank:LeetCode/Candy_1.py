#N children standing in a line
#Each child assigned a rating value
#You give candy to these children according to the following requirements
    #Each child must have at least one piece
    #A child with a higher rating gets more candy than their neighbors
#What is the minimum number of pieces you must give

#Enter a list of integers corresponding to ratings
#Return and integer for the number of pieces of candy

ratings = [int(i) for i in raw_input().strip().split()]

def candy(ratings):
    size = len(ratings)
    candy = [1]*size
    for i in xrange(len(ratings)):
        check(ratings,candy,i, None)
        
    for i in reversed(range(0,size)):
        check(ratings,candy,i,None)
    return sum(candy)
        
        
        
def check(ratings, candy, i,j):
    if j is None:
        check(ratings,candy,i,i-1)
        check(ratings,candy,i,i+1)
    else:
        candy[i] = candy[j] + 1 if (j>=0 and j<len(ratings)) and ratings[i]>ratings[j] and candy[i]<=candy[j] else candy [i]


print candy(ratings)