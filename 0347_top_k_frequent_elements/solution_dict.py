from typing import List 

# runtime: 5.01%, memory: 89.69%
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for val in nums:
            d[val] = d.get(val, 0) + 1
        freqs = sorted(d.keys(), key=d.get, reverse=True)
        return freqs[0:k]
        
