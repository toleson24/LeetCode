from typing import List

# runtine: 94.76%, memory: 23.57%
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length: int = len(height)
        left: int = 0
        right: int = length - 1
        max_water: int = 0

        comp_height = lambda l, h1, h2: h1 * l if h1 < h2 else h2 * l

        for i in range(length):
            water = comp_height(right - left, height[left], height[right])
            if water > max_water:
                max_water = water
            
            if height[left] < height[right]:
                left += 1
            else: right -= 1

        return max_water

        