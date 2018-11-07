"""https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        char_counts = defaultdict(int)
        start = end = length = counter = 0

        while end < len(s):
            end_char = s[end]
            char_counts[end_char] += 1
            if char_counts[end_char] == 1:
                counter += 1
            end += 1

            while counter > 2:
                start_char = s[start]
                char_counts[start_char] -= 1
                if char_counts[start_char] == 0:
                    counter -= 1
                start += 1

            length = max(end - start, length)

        return length


a = Solution()
print(a.lengthOfLongestSubstringTwoDistinct('aa'))
print(a.lengthOfLongestSubstringTwoDistinct('AACBABACDDCDABD'))