""" 171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

https://leetcode.com/problems/excel-sheet-column-number/description/
"""


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for idx, val in enumerate(reversed(s.lower())):
            ans += 26 ** idx * (ord(val) - ord('a') + 1)
        return ans
