from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        visit = deque([(root, 0)])
        vals = []
        while visit:
            cur, depth = visit.popleft()
            if cur:
                if len(vals) == depth:
                    vals.append([cur.val])
                else:
                    vals[depth].append(cur.val)
                visit.append((cur.left, depth+1))
                visit.append((cur.right, depth+1))
        for idx, val in enumerate(vals):
            if idx % 2 == 1:
                vals[idx] = val[::-1]
        return vals
