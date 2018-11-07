"""https://leetcode.com/problems/longest-repeating-character-replacement/description/"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0

        char_counts = defaultdict(int)

        start = end = length = 0

        while end < len(s):
            end_char = s[end]
            char_counts[end_char] += 1
            end += 1
            counter = end - start - max(char_counts.values())

            while counter > k:
                start_char = s[start]
                char_counts[start_char] -= 1
                start += 1
                counter = end - start - max(char_counts.values())

            length = max(length, end - start)
        return length


a = Solution()
print(a.characterReplacement('ABAB', 2))
print(a.characterReplacement('AABABBA', 1))
