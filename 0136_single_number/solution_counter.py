from collections import Counter
from typing import List

# runtime: 33.66%, memory: 7.67%
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)

        res = freq.most_common()[:-2:-1][0][0]
        
        return res

        