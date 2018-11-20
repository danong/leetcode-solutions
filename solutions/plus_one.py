"""https://leetcode.com/problems/plus-one/"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 0:
                break
            digits[i] = digits[i] + carry
            if digits[i] > 9:
                digits[i] = digits[i] % 10
                carry = 1
            else:
                carry = 0
        if carry == 1:
            digits.insert(0, 1)
        return digits
