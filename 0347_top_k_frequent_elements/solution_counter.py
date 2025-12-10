from collections import Counter
from typing import List 

# runtime: 67.62%, memory: 80.14% 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return [k for k, v in counts.most_common(k)]

