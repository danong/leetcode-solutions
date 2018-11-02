"""891. Sum of Subsequence Widths

Given an array of integers A, consider all non-empty subsequences of A.

For any sequence S, let the width of S be the difference between the maximum and minimum element of S.

Return the sum of the widths of all subsequences of A.

As the answer may be very large, return the answer modulo 10^9 + 7.
"""


class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        total = 0
        # for small_idx, small_val in enumerate(A):
        #     for big_idx in range(small_idx + 1, len(A)):
        #         big_val = A[big_idx]
        #         total += (big_val - small_val) << (big_idx - small_idx - 1)
        for idx in range(len(A)):
            total = total << 1
            total -= A[idx]
            total += A[~idx]
        return total % (10 ** 9 + 7)
