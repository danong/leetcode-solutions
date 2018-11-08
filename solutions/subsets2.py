class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        
        nums.sort()
        
        def backtrack(temp, start):
            subsets.append(temp[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                temp.append(nums[i])
                backtrack(temp, i + 1)
                temp.pop()
        
        backtrack([], 0)
        return subsets
