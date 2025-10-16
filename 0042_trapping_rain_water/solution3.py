from typing import List

# runtine: 71.22, memory: 69.51%
class Solution:
    def trap(self, height: List[int]) -> int:
        water: int = 0
        l: int = 0
        r: int = len(height) - 1
        l_max: int = height[l]
        r_max: int = height[r]
        
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                water += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                water += r_max - height[r]

        return water
        
        