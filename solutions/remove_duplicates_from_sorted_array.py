class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # optimal - O(n)
        if len(nums) < 2:
            return len(nums)
        tail = 0
        for i in range(1, len(nums)):
            if nums[tail] != nums[i]:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1
        
        # simple - O(n^2)
        # prev = None
        # for idx in range(len(nums) - 1, -1, -1):
        #     duplicate = prev == nums[idx]
        #     prev = nums[idx]
        #     if duplicate:
        #         del nums[idx]
        # return len(nums)
