from typing import List

# runtime: 87.54%, memory: 60.63%
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        _max: int = 0
        stack: List[int] = []
        length: int = len(heights)

        for i in range(length + 1): 
            curr: int = heights[i] if i < length else 0

            while stack and heights[stack[-1]] > curr:
                h: int = heights[stack.pop()]
                w: int = i if not stack else i - stack[-1] - 1
                _max = max(_max, h * w)
            
            stack.append(i)
        
        return _max

        