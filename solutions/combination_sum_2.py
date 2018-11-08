"""https://leetcode.com/problems/combination-sum-ii/"""

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        combination = []
        
        candidates.sort()
        
        def explore(start, target):
            if target == 0:
                combinations.append(combination[:])
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                explore(i + 1, target - candidates[i])
                combination.pop()
        
        explore(0, target)
        return combinations
