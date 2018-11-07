class Solution:
    def subsets(self, nums):
        """Classic backtracking
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
    
    def subsets_iter(self, nums):
        """Iterative pythonic solution
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        
        for num in nums:
            res.extend([x + [num] for x in res])
            
        return res
