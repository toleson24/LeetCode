from typing import List, Set

# runtime: 74.21%, space: 66.32%
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _set: Set[int] = set(nums)
        _max: int = 0
        
        for n in _set: 
            if n - 1 not in _set:
                l = 1

                while n + l in _set:
                    l += 1

                _max = max(_max, l)
        
        return _max
    
