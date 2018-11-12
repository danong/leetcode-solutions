"""https://leetcode.com/problems/first-missing-positive/"""

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) -1, -1, -1):
            if nums[i] <= 0:
                del nums[i]
        n = len(nums)
        for idx, val in enumerate(nums):
            if val < 0:
                val = val * -1
            if val > n:
                continue
            if nums[val - 1] > 0:
                nums[val - 1] *= -1
        for idx, val in enumerate(nums):
            if val > 0:
                return idx + 1
        return len(nums) + 1
