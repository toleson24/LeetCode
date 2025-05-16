from typing import List

# runtime: 65.89%, memory: 94.84%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit: int = 0
        buy, sell = 0, 1
        length: int = len(prices)

        while sell < length:
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1

        return max_profit

        