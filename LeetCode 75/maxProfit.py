def maxProfit(prices):
    l, r = 0, 1
    res = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            res = max(res, profit)
        
        else: 
            l = r
        r += 1

    return res

prices = [7,1,5,3,6,4]
print(maxProfit(prices))