from typing import List

# runtime: 63.66% , memory: 32.99%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price: int = prices[0]
        _max: int = 0
        
        for p in prices[1:]:
            if p < buy_price:
                buy_price = p
            
            _max = max(_max, p - buy_price)
            
        return _max

        