from typing import List

# runtime: 75.77%, memory: 90.37%
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length: int = len(height)
        _max: int = 0
        left: int = 0
        right: int = length - 1

        while left < right:
            water: int = (right - left) * min(height[left], height[right])
            _max = max(_max, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return _max

        