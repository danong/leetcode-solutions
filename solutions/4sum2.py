"""https://leetcode.com/problems/4sum-ii"""

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        counts = {}
        for a in A:
            for b in B:
                counts[a+b] = counts.get(a+b, 0) + 1
        sols = 0
        for c in C:
            for d in D:
                if -c-d in counts:
                    sols += counts[-c-d]
        return sols
