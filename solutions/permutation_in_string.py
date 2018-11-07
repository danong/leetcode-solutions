from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        char_counts = Counter(s1)
        counter = len(char_counts)

        start_idx = end_idx = 0

        while end_idx < len(s2):
            end_char = s2[end_idx]
            if end_char in char_counts:
                char_counts[end_char] -= 1
                if char_counts[end_char] == 0:
                    counter -= 1
            end_idx += 1

            while counter == 0:
                if (end_idx - start_idx) == len(s1):
                    return True

                start_char = s2[start_idx]
                if start_char in char_counts:
                    char_counts[start_char] += 1
                    if char_counts[start_char] > 0:
                        counter += 1
                start_idx += 1
        return False