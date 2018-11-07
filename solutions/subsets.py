class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(res, temp, nums, start):
            res.append(list(temp))  # append copy of temp to result
            for i in range(start, len(nums)):
                temp.append(nums[i])
                backtrack(res, temp, nums, i + 1)
                temp.pop()
        
        backtrack(res, [], nums, 0)
        return res
