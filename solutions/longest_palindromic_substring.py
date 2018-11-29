"""https://leetcode.com/problems/longest-palindromic-substring/"""

def find_p(s, left, right):
    while 0 <= left <= right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]
    

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = end = 0
        p = ''
        for i in range(len(s)):
            p = max(find_p(s, i, i), find_p(s, i, i+1), p, key=lambda x: len(x))            
        return p
