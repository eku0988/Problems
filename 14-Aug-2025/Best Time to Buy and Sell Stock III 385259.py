# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        
        def dp(index: int, transaction: int, bought: bool) -> int:
            # Base case: no more days OR already used 2 transactions
            if index == len(prices) or transaction == 2:
                return 0
            
            state = (index, transaction, bought)
            if state in cache:
                return cache[state]
            
            # Option 1: Do nothing
            leave = dp(index + 1, transaction, bought)
            
            # Option 2: Buy or Sell
            if bought:
                # Sell: gain price, transaction count +1
                sell = prices[index] + dp(index + 1, transaction + 1, False)
                cache[state] = max(leave, sell)
            else:
                # Buy: pay price, transaction count stays same
                buy = -prices[index] + dp(index + 1, transaction, True)
                cache[state] = max(leave, buy)
            
            return cache[state]
        
        return dp(0, 0, False)
