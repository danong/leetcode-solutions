class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        from functools import lru_cache

        @lru_cache()
        def sum_square(k):
            sum = 0
            for digit in str(k):
                sum += int(digit) ** 2
            return sum

        slow = n
        fast = sum_square(sum_square(n))
        while slow != fast and fast != 1:
            fast = sum_square(sum_square(fast))
            slow = sum_square(slow)
        else:
            return fast == 1