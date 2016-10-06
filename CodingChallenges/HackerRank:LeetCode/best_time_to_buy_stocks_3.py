#Same as the best_time_to_buy_stocks_1,2 but you can comppete
#as many transaction as you like (buy one and sell one share multiple times)
#However, you may not engage in multiple transactions at the same time (you must sell the stock before you buy again)

prices = [int(i) for i in raw_input().strip().split()]


#depending what you did on the previous turn, you can only do one of 2 things on the current turn

#make a dictionary with each key being the level of the tree and each value being a list of tuples
#where first first element of the tuple is the current value from trading
#and the second element is -1 if you bought, +1 if you sold, 0 if you're even

L=[(prices[0],1),(-prices[0],-1),(0,0)]
print L
for i in xrange(1,len(prices)):
    p=prices[i]
    temp_1 = []
    temp_minus1 = []
    temp_zero = []
    for tup in L:
        if tup[1] == 1:
            temp_zero.append((tup[0]-p,0))#buy
            temp_1.append((tup[0],1))#pass
        elif tup[1] == -1:
            temp_zero.append((tup[0]+p,0))#sell
            temp_minus1.append((tup[0],-1))#pass
        else:#tup[0] = 0
            temp_1.append((tup[0]+p,1))#sell
            temp_minus1.append((tup[0]-p,-1))#buy
            temp_zero.append(tup)  
    max_1 = max(temp_1,key=lambda item:item[0])
    max_minus1 = max(temp_minus1,key=lambda item:item[0])
    max_zero = max(temp_zero,key=lambda item:item[0])
    L=[max_1,max_minus1,max_zero]
    print L
    
#Need to finish with a closed out trade so the second term of the tuple must be 0
#The max will be L[2]   
print L[2]
    