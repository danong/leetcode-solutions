"""https://leetcode.com/problems/product-of-array-except-self/"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new = [None] * len(nums)
        new[0] = 1
        for i in range(1, len(nums)):
            new[i] = nums[i - 1] * new[i - 1]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            new[i] *= right
            right *= nums[i]
        return new
