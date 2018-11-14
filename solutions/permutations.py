class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []

        def backtrack(choices, cur):
            print(choices, cur)
            if len(cur) == len(nums):
                output.append(cur[:])
                return

            for val in list(choices):
                cur.append(val)
                choices.remove(val)
                backtrack(choices, cur)
                cur.pop()
                choices.add(val)

        backtrack(set(nums), [])
        return output
