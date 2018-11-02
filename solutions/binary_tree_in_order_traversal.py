# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        visit_queue = []
        curr_node = root
        while visit_queue or curr_node:
            if curr_node:
                visit_queue.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = visit_queue.pop()
                output.append(curr_node.val)
                curr_node = curr_node.right
        return output
