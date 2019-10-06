def maxProfit(prices):
    result = 0
    for i in range(1,len(prices)):
        if prices[i-1] < prices[i]:
            diff = prices[i]-prices[i-1]
            result = max(result+diff,diff)

    return result

prices = [7,6,4,3,1]#[1,2,3,4,5]#[7,1,5,3,6,4]
print(maxProfit(prices))
