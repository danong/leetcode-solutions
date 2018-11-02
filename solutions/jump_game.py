class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reachable = 0
        for idx, val in enumerate(nums):
            if idx > max_reachable:
                return False
            max_reachable = max(max_reachable, idx + val)
        return True