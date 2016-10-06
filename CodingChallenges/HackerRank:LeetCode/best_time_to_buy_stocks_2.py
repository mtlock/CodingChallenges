#Say you have an array for which the ith element is the prince
#of a given stock on day i.
#If you were only permitted to complete at most one transaction
#(i.e., buy one and sell on share of the stock)
#design an algorithm to maximize profit


#@param prices, a list of integers
#@return an integer

def maxProfit(prices):
    if not prices:
        return 0
    max_profit = 0
    min_price = prices[0]
    for i, p in enumerate(prices,start=0):
        max_profit = max(max_profit,(p-min_price))
        min_price = min(min_price,p)
    return max_profit
    
prices = [int(i) for i in raw_input().strip().split()]

print maxProfit(prices)