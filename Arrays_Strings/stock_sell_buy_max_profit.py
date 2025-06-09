# LeetCode #121
# You are given an array prices where prices[i] is the price of a stock on day i.
# You can only buy once and sell once.
# Return the maximum profit you can achieve. If no profit is possible, return 0.


# Output: 5
# → Buy at 1, Sell at 6 → Profit = 6 - 1 = 5

prices = [7,1,5,3,6,4]

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(profit,max_profit)
    return max_profit 

print(max_profit(prices))