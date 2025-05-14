from typing import List

# runtime: 36.23%, memory: 12.52%
class Solution:
    def trap(self, height: List[int]) -> int:
        length: int = len(height)
        
        l_max: List[int] = [0] * length
        r_max: List[int] = [0] * length
        water: List[int] = [0] * length

        _max: int = 0
        for i in range(length - 1):
            if height[i] > _max:
                _max = height[i]
            l_max[i] = _max

        _max = 0
        for i in range(length - 1, 0, -1):
            if height[i] > _max:
                _max = height[i]
            r_max[i] = _max
        
        for i in range(length - 1):
            water[i] = max(min(l_max[i], r_max[i]) - height[i], 0)

        return sum(water)

        