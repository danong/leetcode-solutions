""" 300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?


"""

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = nums[0]
        count = 1
        max_count = 1

        for num in nums[1:]:
            if num > prev:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
            prev = num
            # print(prev, num, count, max_count)
        max_count = max(max_count, count)
        return max_count


if __name__ == '__main__':
    a = Solution()
    a.lengthOfLIS([10,9,2,5,3,7,101,18])