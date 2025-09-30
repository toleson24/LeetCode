from typing import List

# runtime: 47.68%, memory: 90.13%
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i: int = 0
        j: int = len(numbers) - 1
        
        while i < j:
            diff: int = target - numbers[i]
            if numbers[j] == diff:
                return [i + 1, j + 1]
            elif numbers[j] < diff:
                i += 1
            else: # numbers[j] > diff
                j -= 1

        