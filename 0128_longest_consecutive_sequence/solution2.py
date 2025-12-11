from typing import List, Set 

# runtime: 60.57%, memory: 51.98% 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums: Set[int] = set(nums)
        longest: int = 0
        for n in nums:
            if n - 1 not in nums:
                length: int = 0
                while n + length in nums:
                    length += 1
                longest = max(longest, length)
        return longest

        