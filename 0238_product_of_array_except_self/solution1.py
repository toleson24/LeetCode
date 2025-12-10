from typing import List

# runtime: 37.55%, memory: 26.33% 
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
            nums[i] = product
            product *= n

        return [pre * suf for pre, suf in zip(prefix, nums)]

        