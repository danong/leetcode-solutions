"""https://leetcode.com/problems/move-zeroes/"""
class Solution:
    def moveZeroes(self, nums):
        """a
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for idx, val in enumerate(nums):
            nums[idx - zero_count] = val
            if val == 0:
                zero_count += 1
        for idx in range(len(nums) - 1, len(nums) - 1 - zero_count, -1):
            nums[idx] = 0
