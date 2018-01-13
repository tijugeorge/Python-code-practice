

def maxProfit(prices):
  min_price, max_profit = float('inf'), 0
  for price in prices:
    min_price = min(price, min_price)
    profit = price - min_price
    max_profit = max(max_profit, profit)
  return max_profit
  
  
prices = [7, 1, 5, 3, 6, 4]

print(maxProfit(prices))
