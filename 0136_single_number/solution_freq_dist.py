from typing import Dict, List

# runtime: 47.04%, memory: 23.71%
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fd: Dict[int, int] = {}
        for n in nums:
            if n not in fd:
                fd[n] = 1
            else:
                fd[n] += 1
        
        for k in fd.keys():
            if fd[k] == 1:
                return k

        