# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        visit_stack = []
        cur_node = root
        seen = 0
        while visit_stack or cur_node:
            # take left path
            if cur_node:
                visit_stack.append(cur_node)
                cur_node = cur_node.left
            #
            else:
                cur_node = visit_stack.pop()
                seen += 1
                if seen == k:
                    return cur_node.val
                cur_node = cur_node.right
