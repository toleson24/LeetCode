from typing import List, Set 

# runtime: 44.52%, memory: 29.43%
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s : Set[int] = set(nums)
        return len(s) < len(nums)
