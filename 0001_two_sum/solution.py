from typing import List


def twoSum(self, nums: List[int], target: int):
    """
    :type nums: List[int]
    :type target: int
    :rtype List[int]
    """
    d = {}
    for idx, val in enumerate(nums):
        dif = target - nums[idx]
        if dif in d:
            return idx, d[dif]
        d[nums[idx]] = idx

