class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        from math import factorial
        m = m - 1
        n = n - 1
        total_moves = m + n
        return round(factorial(total_moves) / factorial(n) / factorial(m))
