# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a_ptr = l1
        b_ptr = l2
        carry = False
        sum_root = sum_ptr = ListNode(x=None) # dummy node
        while a_ptr or b_ptr:
            a_val = a_ptr.val if a_ptr else 0
            b_val = b_ptr.val if b_ptr else 0
            sum_val = a_val + b_val + int(carry)
            if sum_val > 9:
                sum_val = sum_val % 10
                carry = True
            else:
                carry = False
            sum_ptr.next = ListNode(sum_val)
            sum_ptr = sum_ptr.next
            if a_ptr:
                a_ptr = a_ptr.next
            if b_ptr:
                b_ptr = b_ptr.next
        if carry:
            sum_ptr.next = ListNode(1)
        return sum_root.next