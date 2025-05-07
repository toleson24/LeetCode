from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        left: int = 1
        right: int = max(piles)
        
        while left < right:
            mid: int = (left + right) // 2
            total: int = 0

            for pile in piles:
                total += (pile + mid - 1) // mid
            
            if total <= h:
                right = mid
            else:
                left = mid + 1
        
        return left

        