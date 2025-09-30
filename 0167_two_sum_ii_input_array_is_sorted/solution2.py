from typing import List

# runtime: 23.42%, memory: 100.00%
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        left = 0
        right = l - 1
        while right >= 0 and left < l and numbers[left] + numbers[right] != target:
            if target - numbers[right] > numbers[left]:
                left += 1
            else:
                right -= 1
        return left + 1, right + 1
    
        