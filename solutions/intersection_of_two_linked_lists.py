# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def list_len(root):
    count = 0
    while root:
        root = root.next
        count += 1
    return count


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :param headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        a_ptr = headA
        b_ptr = headB
        while a_ptr != b_ptr:
            a_ptr = headB if a_ptr is None else a_ptr.next
            b_ptr = headA if b_ptr is None else b_ptr.next
        return a_ptr
