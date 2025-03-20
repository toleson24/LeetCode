from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets: List[int] = []
        length: int = len(nums)

        nums.sort()

        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j: int = i + 1
            k: int = length - 1
            while j < k:
                _sum: int = nums[i] + nums[j] + nums[k]
                if _sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif _sum < 0:
                    j += 1
                else:  # _sum > 0:
                    k -= 1

        return triplets

        