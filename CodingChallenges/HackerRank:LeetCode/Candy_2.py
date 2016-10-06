#N children standing in a line
#Each child assigned a rating value
#You give candy to these children according to the following requirements
    #Each child must have at least one piece
    #A child with a higher rating gets more candy than their neighbors
#What is the minimum number of pieces you must give

#Enter a list of integers corresponding to ratings
#Return and integer for the number of pieces of candy


ratings = [int(i) for i in raw_input().strip().split()]


candy = [1]*len(ratings)
if ratings[0]>ratings[1]:
    candy[0]=2



for i in range(1,len(candy)):
    if ratings[i]<ratings[i-1]:
        candy[i]=1
        if candy[i-1]==1:
            j=i
            while candy[j]-candy[j-1]==0:
                candy[j-1]=candy[j-1]+1
                j=j-1
        
    elif ratings[i]==ratings[i-1]:
        candy[i]=1#candy[i-1]
    else:#ratings[i]>ratings[i-1]
        candy[i]=candy[i-1]+1

print sum(candy)
        
        
        
        
    