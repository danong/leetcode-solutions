"""https://leetcode.com/problems/find-the-duplicate-number/"""

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time: O(N^2), space: O(N)
        # for idx in range(len(nums) - 1):
        #     for idx2 in range(idx + 1, len(nums)):
        #         if nums[idx] == nums[idx2]:
        #             return nums[idx]
        # return None

        slow_idx = nums[0]
        fast_idx = nums[slow_idx]
        print(slow_idx, fast_idx)
        while slow_idx != fast_idx:
            slow_idx = nums[slow_idx]
            fast_idx = nums[nums[fast_idx]]
        fast_idx = 0
        while slow_idx != fast_idx:
            fast_idx = nums[fast_idx]
            slow_idx = nums[slow_idx]
        return slow_idx
