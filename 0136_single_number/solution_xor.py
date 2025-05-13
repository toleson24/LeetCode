from typing import List

# runtime: 66.15%, memory: 44.58%
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result: int = 0
        for num in nums:
            result ^= num
        
        return result

        