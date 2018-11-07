"""Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def bin_search(array, val, left_idx, right_idx):
            """Return idx of val in array or None"""
            if left_idx > right_idx:
                return None

            mid_idx = ((right_idx - left_idx) // 2) + left_idx
            if array[mid_idx] == val:
                return mid_idx
            elif array[mid_idx] > val:
                return bin_search(array, val, left_idx, mid_idx - 1)
            else:
                return bin_search(array, val, mid_idx + 1, right_idx)

        if len(nums) < 3:
            return []
        solutions = set()
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while (right - left) > 1:
            c = 0 - nums[left] - nums[right]
            c_idx = bin_search(nums, c, left + 1, right - 1)
            if c_idx:
                solutions.add((nums[left], nums[c_idx], nums[right]))
            if c > 0:
                left += 1
            else:
                right -= 1
        return [list(x) for x in solutions]


a = Solution()
print(a.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
# print(a.threeSum([-1, 0, 1, 2, -1, -4, 10, -8, 4, 76, -9, -23, -15, 0]))
# print(a.threeSum([0, 0, 0, 0]))
