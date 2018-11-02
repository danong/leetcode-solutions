class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        next_0 = 0
        next_2 = len(nums) - 1
        for idx in range(len(nums)):
            while nums[idx] == 0 or nums[idx] == 2:
                if nums[idx] == 0:
                    if idx < next_0:
                        break
                    nums[next_0], nums[idx] = nums[idx], nums[next_0]
                    next_0 += 1
                else:
                    if idx > next_2:
                        break
                    nums[idx], nums[next_2] = nums[next_2], nums[idx]
                    next_2 -= 1