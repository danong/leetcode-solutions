""" 788. Rotated Digits

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].

"""

# brute force
class Solution:
    rotation_mapping = {
        0: 0,
        1: 1,
        2: 5,
        5: 2,
        6: 9,
        8: 8,
        9: 6,
    }

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for x in range(1, N + 1):
            if self.is_valid(x):
                count += 1
        return count

    def is_valid(self, x):
        new_digits = []
        for digit in str(x):
            if int(digit) in self.rotation_mapping:
                new_digits.append(self.rotation_mapping[int(digit)])
            else:
                return False
        return int(''.join(map(str, new_digits))) != x