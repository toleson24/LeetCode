from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)

        res = freq.most_common()[:-2:-1][0][0]
        
        return res

        