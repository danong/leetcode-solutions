"""https://leetcode.com/problems/reverse-linked-list/"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# null -> 1 -> 2 -> 3 -> null
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur != None:
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n
        return prev
