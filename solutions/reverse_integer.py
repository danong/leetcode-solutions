"""https://leetcode.com/problems/reverse-integer/submissions/"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1, -1][x < 0]
        x *= sign
        res = 0
        while x:
            t = x % 10
            x = x // 10
            res = res * 10 + t
        res *= sign
        if -2**31 <= res <= 2**31-1:
            return res
        else:
            return 0
