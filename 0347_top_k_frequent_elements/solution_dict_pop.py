from typing import List 

# runtime: 5.01%, memory: 96.52% 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for val in nums:
            d[val] = d.get(val, 0) + 1
        
        for i in range(k):
            key = max(d, key=d.get)
            d.pop(key) 
            nums[i] = key

        return nums[:k] 

