class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l = len(nums)
        if l <= 0:
            return False

        # nums.sort()
        # i = 0
        # for i in range(0, l):
        #     j = 1
        #     while nums[j] == nums[i] and j < l:
        #         if abs(i - j) <= k:
        #             return True
        #         j += 1
        # return False

        # k_idx = {}
        # i = 0
        # for i in range(0, l):
        #     k_idx.update({i: nums[i]})
        # keys = k_idx.keys()
        # i = 0
        # for i in range(0, l):
        #     j = 1
        #     for j in range(1, l):
        #         if abs(keys[i] - keys[j]) <= k and k_idx[keys[i]] == k_idx[keys[j]]:
        #             return True
        # return False

        i = 0
        for i in range(l):
            j = i + 1
            for j in range(i + 1, l):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False

        