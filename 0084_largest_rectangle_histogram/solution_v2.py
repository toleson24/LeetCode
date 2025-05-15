from typing import List, Tuple
from itertools import chain

# neetcode style
# runtime: 43.07%, memory: 24.43% 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        _max: int = 0
        stack: List[Tuple[int, int]] = []
        
        for idx, height in enumerate(chain(heights, [0])):
            start: int = idx

            while start and stack[-1][1] > height:
                i, h = stack.pop()
                _max = max(_max, (idx - i) * h)
                start = i
            
            stack.append((start, height))
        
        return _max

        