from typing import List

# runtime: 48.36, memory: 35.88% 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix: List[int] = [_ for _ in range(len(nums))]
        product: int = 1
        for i, n in enumerate(nums):
            prefix[i] = product
            product *= n

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            n: int = nums[i]
            nums[i] = product * prefix[i]
            product *= n

        return nums

        