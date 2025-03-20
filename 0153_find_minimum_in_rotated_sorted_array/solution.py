from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1
        while left < right:
            mid: int = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:  # nums[mid] >= right
                left = mid + 1
        return nums[left]

        