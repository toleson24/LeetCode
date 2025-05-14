from typing import List

# runtime: 100.00%, memory: 93.21%
class Solution:
    def trap(self, height: List[int]) -> int:
        water: int = 0

        left: int = 0
        right: int = len(height) - 1
        l_max: int = 0
        r_max: int = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= l_max:
                    l_max = height[left]
                else:
                    water += l_max - height[left]
                left += 1
            else:
                if height[right] >= r_max:
                    r_max = height[right]
                else:
                    water += r_max - height[right]
                right -= 1

        return water

        