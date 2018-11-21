"""https://leetcode.com/problems/longest-consecutive-sequence/"""
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0
        for i in nums:
            if i - 1 in num_set:
                continue
            y = i + 1
            while y in num_set:
                y += 1
            longest = max(longest, y - i)
        return longest
