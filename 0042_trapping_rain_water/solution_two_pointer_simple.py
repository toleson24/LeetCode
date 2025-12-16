from typing import List 

# runtime: 97.15%, memory: 69.04%
class Solution:
    def trap(self, height: List[int]) -> int:
        water: int = 0

        left: int = 0
        right: int = len(height) - 1
        l_max: int = 0
        r_max: int = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] > l_max:
                    l_max = height[left]
                water += l_max - height[left]
                left += 1
            else: 
                if height[right] > r_max:
                    r_max = height[right]
                water += r_max - height[right]
                right -= 1

        return water

        