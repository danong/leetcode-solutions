"""234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        mid_ptr = end_ptr = head
        while end_ptr and end_ptr.next:
            end_ptr = end_ptr.next.next
            rev, rev.next, mid_ptr = mid_ptr, rev, mid_ptr.next
        if end_ptr:
            mid_ptr = mid_ptr.next
        while mid_ptr and rev.val == mid_ptr.val:
            mid_ptr = mid_ptr.next
            rev = rev.next
        return not rev
