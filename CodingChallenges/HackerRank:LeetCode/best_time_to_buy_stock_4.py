#Same as before, but now can only make at most 2 transactions

price = [int(i) for i in raw_input().strip().split()]

#3-tuple (how much money, buy/sell/even,number of transactions)
#-1 for buy, +1 sell, 0 even


L=[(price[0],1,.5),(-price[0],-1,.5),(0,0,0)]
maxProfit = 0
numtrades = [0,.5]

for i in xrange(1,len(price)):
    temp = L
    L = []
    L0 = []
    L1 = []
    Lneg1 = []
    for item in temp:
        if item[1] == 1:
            L1.append(item)
            if item[2]+.5 == 2 and item[0]-price[i]>maxProfit:
                maxProfit = item[0]-price[i]
            else:
                L0.append((item[0]-price[i],0,item[2]+.5))
                if item[2]+.5 not in numtrades:
                    numtrades.append(item[2]+.5)
        elif item[1] == -1:
            Lneg1.append(item)
            if item[2]+.5 == 2 and item[0]+price[i]>maxProfit:
                maxProfit = item[0]+price[i]
            else:
                L0.append((item[0]+price[i],0,item[2]+.5))
                if item[2]+.5 not in numtrades:
                    numtrades.append(item[2]+.5)
        else:#item[1] == 0
            L0.append(item)
            L1.append((item[0]+price[i],1,item[2]+.5))
            Lneg1.append((item[0]-price[i],-1,item[2]+.5))
            if item[2]+.5 not in numtrades:
                numtrades.append(item[2]+.5)
                
    
    for n in numtrades:
        max1 = 0
        max0 = 0
        maxneg1 = 0
        for item in L1:
            if item[2] == n and item[0]>max1:
                max1 = item[0]
        if max1>0:
            L.append((max1,1,n))
        for item in L0:
            if item[2] == n and item[0]>max0:
                max0 = item[0]
        if max0>0:
            L.append((max0,0,n))
        for item in Lneg1:
            if item[2] == n and item[0]>maxneg1:
                maxneg1 = item[0]
        if maxneg1>0:
            L.append((maxneg1,-1,n))
        
print "The max profit is ", max(maxProfit,max(L0)[0])
        
                
       
    

            
                
