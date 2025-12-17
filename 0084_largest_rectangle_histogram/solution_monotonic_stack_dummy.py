from typing import List 

# runtime: 91.80%, memory: 59.58% 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List[int] = [-1]
        heights.append(0)
        max_area: int = 0

        for i, curr_height in enumerate(heights):
            while stack and heights[stack[-1]] > curr_height:
                height: int = heights[stack.pop()]
                width: int = i - stack[-1] - 1
                max_area = max(max_area, width * height)
            
            stack.append(i)
            
        return max_area

        