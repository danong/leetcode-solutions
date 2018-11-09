"""https://leetcode.com/problems/combination-sum/"""

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        combination = []
        
        def explore(start, target):
            if target == 0:
                combinations.append(combination[:])
                return
            
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                explore(i, target - candidates[i])
                combination.pop()
                
        explore(0, target)
        return combinations
