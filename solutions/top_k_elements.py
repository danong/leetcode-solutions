"""https://leetcode.com/problems/top-k-frequent-elements"""

import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type key: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        # pythonic
        # return [x[0] for x in counts.most_common(k)]
        min_heap = []
        for key, val in counts.items():
            heapq.heappush(min_heap, (val, key))
            while len(min_heap) > k:
                heapq.heappop(min_heap)
        return [x[1] for x in reversed(min_heap)]
