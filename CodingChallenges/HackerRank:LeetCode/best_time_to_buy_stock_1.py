#Say you have an array for which the ith element is the prince
#of a given stock on day i.
#If you were only permitted to complete at most one transaction
#(i.e., buy one and sell on share of the stock)
#design an algorithm to maximize profit

prices = [int(i) for i in raw_input().strip().split()]


#In the case that you can sell before you buy

max = prices[0]
min = prices[0]
for i in xrange(1,len(prices)):
    if prices[i] > max:
        max = prices[i]
    if prices[i] < min:
        min = prices[i]
print max-min


#In the case that you must buy before you sell (or on same day in case price decreases always)
def P(L):
    max = 0
    min = 0
    p = L[max] - L[min]
    for i in xrange(max,len(prices)):
        if L[i] < L[max]:
            continue
        else:
            for j in xrange(i,len(prices)):
                if L[i] - L[j] > p:
                    max = i
                    min = j
                    p = L[i] - L[j]
    return p

print P(prices)
    
